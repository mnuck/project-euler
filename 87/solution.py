#!/usr/bin/env python
#
# Project Euler 87

'''
How many numbers below fifty million can be expressed
as the sum
of a prime square, prime cube, and prime fourth power?

Strategy: Generate a list of all possible candidate prime squares,
a list of a possible candidate prime cubes, and a list of all
possible candidate prime fourths. Add em up.
'''

from bitarray import bitarray
from math import sqrt, pow

max_num = 50000000


def generate_primes():
    size = max_num * 2
    stop = int(sqrt(size))
    a = bitarray(size)
    a.setall(True)
    a[:2] = False
    primes = list()
    next = 2
    try:
        while True:
            primes.append(int(next))
            if next < stop:
                a[next::next] = False
            next = a.index(True, next + 1)
    except ValueError:
        pass
    return primes

primes = generate_primes()
squares = [int(pow(x, 2)) for x in primes]
cubes = [int(pow(x, 3)) for x in primes]
fours = [int(pow(x, 4)) for x in primes]

result = set()

for f in fours:
    partial = f
    if partial > max_num:
        break
    for c in cubes:
        partial = f + c
        if partial > max_num:
            break
        for s in squares:
            candidate = partial + s
            if candidate < max_num:
                result.add(candidate)

print len(result)
