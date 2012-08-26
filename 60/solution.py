#!/usr/bin/env python
#
# Project Euler 60

from itertools import combinations
from bitarray import bitarray
from math import sqrt

primes = None
primeset = None

maxlen = 8

def generate_primes():
    global maxlen
    size = 10 ** maxlen
    stop = int(sqrt(size))

    a = bitarray(size)
    a.setall(True)
    a[:2] = False # 0, 1 are not prime

    primes = list()
    next = 2L
    try:
        while True:
            primes.append(next)
            if next < stop:
                a[next::next] = False
            next = a.index(True, next+1)
    except ValueError:
        pass
    return primes


def pair_satisfies(a, b):
    global primeset
    a, b = str(a), str(b)
    i, j = int(a + b), int(b + a)
    return i in primeset and j in primeset


def set_satisfies(s):
    if len(s) < 2:
        return True
    return all(pair_satisfies(a, b) for (a, b) in combinations(s, 2))


dead_ends = set()

def partial(working):
    global maxlen
    if len(working) == 5:
        return working

    if len(working) > 0:
        longest = max(working, key=lambda x: len(str(x)))
        maxprime = 10 ** (maxlen - len(str(longest)))
    else:
        maxprime = 10 ** maxlen
    
    for prime in primes:
        if prime > maxprime:
            break
        if prime in [2, 5]:
            continue
        if prime in working:
            continue
        next_attempt = list(working)
        next_attempt.append(prime)
        if frozenset(next_attempt) in dead_ends:
            continue
        if not set_satisfies(next_attempt):
            continue
        result = partial(next_attempt)
        if result:
            return result
    dead_ends.add(frozenset(working))
    return False

    
def solution():
    global primes
    global primeset
    print "generating primes..."
    primes = generate_primes()
    print "prepping O(1) prime lookup table..."
    primeset = set(primes)
    print "solving..."
    return sum(partial([]))


if __name__ == "__main__":
    print solution()
