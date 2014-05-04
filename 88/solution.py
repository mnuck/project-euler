#!/usr/bin/env python
# hello beloved.  I'm typing away.
#
# Project Euler 88

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


def product_sum_set_size(factors):
    partial_sum = sum(factors)
    N = reduce(lambda x,y: x*y, factors)
    ones = N - partial_sum
    return len(factors) + ones


combo_cache = dict()

def generate_factor_combinations(factors):
    global combo_cache
    factors = tuple(sorted(factors))
    if factors in combo_cache:
        return combo_cache[factors]
    result = set()
    result.add(factors)
    if len(factors) > 2:
        for i in xrange(len(factors) - 1): # {2, 3, 5, 7}
            for j in xrange(i+1, len(factors)):
                nextfactors = list(factors[:i]) + list(factors[i+1:j])
                if j != len(factors) - 1:
                    nextfactors += list(factors[j+1:])
                product = factors[i] * factors[j]
                nextfactors.append(product)
                child = generate_factor_combinations(nextfactors)
                result = result.union(child)
    combo_cache[factors] = result
    return combo_cache[factors]


def product_sum_set_sizes(N):
    prime_factors = factorize(N)
    factor_sets = generate_factor_combinations(prime_factors)
    return [product_sum_set_size(x) for x in factor_sets]


def solution():
    minimal_product_sums = dict()  # k -> N 
    for N in xrange(2, 24000):  # may need to increase a lot
        for k in product_sum_set_sizes(N):
            if k not in minimal_product_sums:
                minimal_product_sums[k] = N
    
    resultset = set()
    for i in xrange(2, 12001):
        resultset.add(minimal_product_sums[i])

    return sum(resultset)


if __name__ == "__main__":
    print solution()

