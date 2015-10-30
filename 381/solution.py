#!/usr/bin/env python
#
# Project Euler 381
#
# http://arxiv.org/ftp/math/papers/0703/0703354.pdf

"""
For a prime p let S(p) = (\sum{(p-k)!)} mod(p) for 1 <= k <= 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! 
= 720+120+24+6+2 
= 872.

As 872 mod(7) = 4, S(7) = 4.

It can be verified that \sum{S(p)} = 480 for 5 <= p < 100.

Find \sum{S(p)} for 5 <= p < 10**8.
"""

import bitarray
import itertools

from math import sqrt

def primes(maxP):
    stop = int(sqrt(maxP))
    a = bitarray.bitarray(maxP)
    a.setall(True)
    a[:2] = False
    next = 2
    try:
        while True:
            yield next
            if next < stop:
                a[next::next] = False
            next = a.index(True, next+1)
    except ValueError:
        pass

def bigS(p):
    h = p / 24
    r = p - (24 * h)
    a = (r * h) + (r*r - 1)/24 % p

    b = a * (p-4)
    c = b * (p-3) # c % p = (p - 1) / 2
    #d = 0 # c * (p-2) # d % p = 1
    #e = 0 #d * (p-1) # e % p = p - 1
    # d + e = p. p % p = 0
    return (a + b + c) % p

def solution():
    return sum(bigS(p) for p in primes(pow(10, 8)) if p >= 5)

if __name__ == "__main__":
    print solution()