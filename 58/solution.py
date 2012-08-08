#!/usr/bin/env python
#
# Project Euler 58

from bitarray import bitarray
from math import sqrt

def generate_primes():
    size = 10 ** 9
    stop = int(sqrt(size))

    a = bitarray(size)
    a.setall(True)
    a[:2] = False

    primes = list()
    next = 2
    try:
        while True:
            primes.append(next)
            if next < stop:
                a[next::next] = False
            next = a.index(True, next+1)
    except ValueError:
        pass
    return primes


def diagonals(n):
    return [n*n, 
            n*n -   (n-1),
            n*n - 2*(n-1), 
            n*n - 3*(n-1)]


def solution():
    primes = set(generate_primes())
    
    prime_count = 0
    diag_count = 1
    ratio = 999.0
    n = 1
    while ratio > 0.1:
        n += 2
        prime_count += len([x for x in diagonals(n) if x in primes])
        diag_count  += 4
        ratio = float(prime_count) / diag_count
    
    return n

if __name__ == "__main__":
    print solution()
