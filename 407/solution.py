#!/usr/bin/env python
#
# Project Euler 407
#
# http://www.artofproblemsolving.com/community/c1142h1038152_idempotents

"""
If we calculate a*a mod 6 for 0 <= a <= 5 we get: 0,1,4,3,4,1.

The largest value of a such that a*a ~= a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a*a ~= a (mod n).
So M(6) = 4.

Find \sum{M(n)} for 1 <= n <= pow(10,7).
"""

import bitarray
import math

import math
import itertools

def genPrimes(size):
    stop = int(math.sqrt(size))
    a = bitarray.bitarray(size)
    a.setall(True)
    a[:2] = False
    next = 2
    try:
        while True:
            yield int(next)
            if next < stop:
                a[next::next] = False
            next = a.index(True, next+1)
    except ValueError:
        pass

primes = set()
factors = dict()

def factorize(n):
    global primes
    global factors
    if n in factors:
        return factors[n]
    result = dict()
    original = n
    if n in primes:
        factors[n] = {n: 1}
        return factors[n]
    for prime in primes:
        while n % prime == 0:
            if prime not in result:
                result[prime] = 0
            result[prime] += 1
            n /= prime
            if n in factors:
                for k in factors[n].iterkeys():
                    if k not in result:
                        result[k] = 0
                    result[k] += factors[n][k]
                factors[original] = result
                return factors[original]
    return {1: 1}

def totient(d):
    result = 1
    if d == 1:
        return result
    factors = factorize(d)
    for prime, exponent in factors.iteritems():
        result *= (prime - 1)
        if exponent > 1:
            result *= pow(prime, (exponent - 1))
    return result

def CRT(coefficients, moduli, M):
    """solves chinese remainder theorem"""
    result = 0
    for (a, m) in zip(coefficients, moduli):
        b = M / m
        bp = pow(b, totient(m) - 1, m)
        result +=  a * b * bp
    return result

def bigM(n):
    """largest value of a such that a*a % n ~= a mod n"""
    if len(factorize(n)) == 1:
        return 1
    return max(getIdempotents(n))

def getIdempotents(n):
    factors = [pow(p,e) for (p, e) in factorize(n).iteritems()]
    M = reduce(lambda x, y: x * y, factors)
    return [CRT(coefficients, factors, M) % M
            for coefficients 
            in itertools.product([0, 1], repeat=len(factors))]

def solution(size):
    global primes
    primes = set(genPrimes(size))
    return sum(bigM(x) for x in xrange(2, size))

if __name__ == "__main__":
    print solution(1 + pow(10, 7))