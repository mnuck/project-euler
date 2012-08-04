#!/usr/bin/env python
#
# Project Euler 38

def isPandigital(s):
    return sorted(s) == ['1','2','3','4','5','6','7','8','9']

def generate(i):
    j, result = 1, ""
    while len(result) < 9:
        result += str(i*j)
        j += 1
    return result

print max(filter(isPandigital, map(generate, xrange(1,1000000))))
