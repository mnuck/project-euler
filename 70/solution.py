#!/usr/bin/env python
#
# Project Euler 70

from bitarray import bitarray
from math import sqrt

def generate_primes():
    size = 10 ** 7
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
            next = a.index(True, next+1)
    except ValueError:
        pass
    return primes

primes = set(generate_primes())
factors = dict()

def factorize(n):
    global primes
    global factors
    result = list()
    original = n
    if n in primes:
        factors[n] = [n]
        return factors[n]
    for prime in primes:
        while n % prime == 0:
            result.append(prime)
            n /= prime
            if n in factors:
                factors[original] = result + factors[n]
                return factors[original]

def totient(d):
    result = 1
    factors = factorize(d)
    used = set()
    for factor in factors:
        if factor in used:
            result *= factor
        else:
            result *= (factor - 1)
            used.add(factor)
    return result


def are_permutations(a, b):
    return sorted(str(a)) == sorted(str(b))


def solution():
    min_ratio = 99999999
    result = None
    for n in xrange(2, 10 ** 7):
        t = totient(n)
        ratio = n / float(t)
        if ratio < min_ratio:
            if are_permutations(n, t):
                min_ratio = ratio
                result = n
                print "possible solution:", n
    return result


if __name__ == "__main__":
    print solution()
