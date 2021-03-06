#!/usr/bin/env python
#
# Project Euler 78

from math import pow
p_cache = {0: 1}


def p(n):
    if n < 0:
        return 0
    if n not in p_cache:
        result = 0
        k = 1
        while p(n - g(k)) != 0:
            result += p(n - g(k)) * int(pow(-1, (k - 1)))
            k += 1
        k = -1
        while p(n - g(k)) != 0:
            result += p(n - g(k)) * int(pow(-1, (k - 1)))
            k -= 1
        p_cache[n] = result
    return p_cache[n]


def g(k):
    return k * (3 * k - 1) / 2


def solution():
    n = 1
    while p(n) % 1000000 != 0:
        n += 1
    return n


if __name__ == "__main__":
    print solution()
