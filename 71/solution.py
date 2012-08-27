#!/usr/bin/env python
#
# Project Euler 71

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
    if n in factors:
        return factors[n]
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
    return [1]

            
def get_numerators(denominator, min_val, max_val):
    result = list()
    d_factors = set(factorize(denominator))
    min_num = int(denominator * min_val) + 1
    max_num = int(denominator * max_val)
#    print min_num, max_num
    for n in xrange(min_num, max_num + 1):
#    for n in xrange(1, denominator):
        n_factors = set(factorize(n))
        if not (n_factors.intersection(d_factors)):
            result.append(n)
    return result


def fractions(denominator, min_val, max_val):
    result = list()
    numerators = get_numerators(denominator, min_val, max_val)
    for n in numerators:
        value = float(n) / denominator
        if value >= min_val and value <= max_val:
#            print value
            result.append({'n': n,
                           'd': denominator,
                           'v': float(n) / denominator})
    return result

def solution():
    min_val = 299999.0 / 700000.0
    max_val = 3000.0 / 7000.0
    result = list()
    for denominator in xrange(2, 1000001):
        result.extend(fractions(denominator, min_val, max_val))
    result.sort(key = lambda x: x['v'])
    return result[-2]['n']

if __name__ == "__main__":
    print solution()
