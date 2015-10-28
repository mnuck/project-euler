#!/usr/bin/env python
#
# Project Euler 111

import itertools

def tryComposite(a, d, n, s):
    x = pow(a, d, n)
    if x in [1, n - 1]:
        return False
    for i in xrange(1, s):
        x = pow(x, 2, n)
        if x == n - 1:
            return False
    return True

def isPrime(n):
    if n in [2, 3]:
        return True
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d / 2
        s = s + 1
    # magic numbers from http://miller-rabin.appspot.com/
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a > (n - 2):
            return True
        if tryComposite(a, d, n, s):
            return False
    return True

def repeaters(d, m, n):
    """Yields the set of numbers
       of length n digits
       with m digits be d"""
    minRepeater = pow(10, n - 1)
    seen = set()
    suffix_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    del suffix_digits[d]
    prefix = str(d) * m
    for suffix in itertools.combinations_with_replacement(suffix_digits, n - m):
        digits = prefix + ''.join(suffix)
        for repeater in itertools.permutations(digits):
            if repeater not in seen and repeater[0] != '0':
                seen.add(repeater)
                yield int(''.join(repeater))

def repeaterPrimes(d, m, n):
    """Yields the set of prime numbers
       of length n digits
       with m digits being d"""
    for x in repeaters(d, m, n):
        if isPrime(x):
            yield x

def bigS(n, d):
    result = 0
    m = n - 1
    done = False
    while m > 0 and not done:
        for r in repeaterPrimes(d, m, n):
            done = True
            result += r
        m = m - 1
    return result

def solution(n):
    return sum(bigS(n, i) for i in xrange(10))


if __name__ == "__main__":
    print solution(10)