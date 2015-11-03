#!/usr/bin/env python
#
# Project Euler 124
#

"""
The radical of n, rad(n), is the product of the distinct prime factors
of n. For example, 504 = 2^3 * 3^2 * 7, so rad(504) = 2 * 3 * 7 = 42.

If we calculate rad(n) for 1 <= n <= 10, then sort them on rad(n),
and sorting on n if the radical values are equal, we get this here chart
that I didn't include, but you can find on the website.

Let E(k) be the kth element in the sorted n column; 
for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 <= n <= 100000, find E(10000).
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

def rad(n):
    return reduce(lambda x,y: x*y, factorize(n).iterkeys())

def solution(size):
    global primes
    primes = set(genPrimes(size*2))
    [factorize(x) for x in xrange(1, size)]

    E = [(n, rad(n)) for n in xrange(1, size)]
    E.sort(key=lambda x: (x[1], x[0]))
    return E[9999]

if __name__ == "__main__":
    print solution(1 + pow(10, 5))[0]