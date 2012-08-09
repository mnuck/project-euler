#!/usr/bin/env python
#
# Project Euler 72

from bitarray import bitarray
from math import sqrt

def generate_primes():
    size = 1000000
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
    
def valid_numerator_count(d):
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

def solution():
    return sum( [valid_numerator_count(x) for x in xrange(2,1000001)] )

if __name__ == "__main__":
    print solution()
