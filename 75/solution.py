#!/usr/bin/env python
#
# Project Euler 75
# Uses Euclid's formula for generating Pythagorean triples

from math import sqrt
from fractions import gcd
size = 1500000


def gen_triples(stop):
    m, n = 2, 1
    m_too_big = int(sqrt(size / 2))
    while m < m_too_big:
        yield (m, n)
        n += 2
        while gcd(m, n) != 1:
            n += 2
        if 2 * m * (m + n) > stop or n > m:
            m += 1
            n = m % 2 + 1


def solution():
    result = [0] * (size + 1)
    for (m, n) in gen_triples(size):
        base = 2 * m * (m + n)
        next = base
        while next <= size:
            result[next] += 1
            next += base
    return len([x for x in result if x == 1])


if __name__ == "__main__":
    print solution()
