#!/usr/bin/env python

from itertools import combinations
from bitarray import bitarray
from math import sqrt

digits = 6

def generate_primes():
    size = 10 ** digits
    stop = int(sqrt(size))

    a = bitarray(size)
    a.setall(True)
    a[:2] = False

    primes = list()
    next = 2
    try:
        while True:
            s = str(next)
            if len(s) == digits:
                primes.append(str(next))
            if next < stop:
                a[next::next] = False
            next = a.index(True, next+1)
    except ValueError:
        pass
    return primes


def sub_a_digit(base, digit, indexes):
    """Substitutes digit into base at the requested indexes"""
    result = list(base)
    for i in indexes:
        result[i] = digit
    return "".join(result)


def sub_all_digits(base, indexes):
    """Substitutes all digits into base at the requested indexes"""
    return [sub_a_digit(base, d, indexes) for d in "0123456789"]


def rate(base, primes):
    max_index = len(base)
    family_size = 1
    for changes in xrange(1,max_index+1):
        indexeses = combinations(range(max_index),changes)
        for indexes in indexeses:
            family_size = max([family_size,
                               len([x for x in sub_all_digits(base, indexes) 
                                    if x in primes])])
            print [x for x in sub_all_digits(base, indexes) if x in primes]
#    return family_size
        

def solution():
    primes = generate_primes()
    max_family_size = 1
    winner = 0
    i = -1
    for prime in primes:
        i += 1
        rating = rate(prime, primes)
        if i % 50 == 0:
            print i, rating, prime
        if rating > max_family_size:
            max_family_size = rating
            winner = prime
            print "WINNING", rating, winner
            if max_family_size == 8:
                print "WINNAR!", winner
                exit()
    print "BEST", max_family_size, winner

def derp():
    primes = generate_primes()
    print rate("120383", primes)
    
if __name__ == "__main__":
    #solution()
    derp()
