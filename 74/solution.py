#!/usr/bin/env python
#
# Project Euler 74

factorial = [ 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 ]

cache = dict()

def chain(n):
    global factorial
    global cache
    original = n
    result = set()
    while not n in result:
        result.add(n)
        n = sum([factorial[int(x)] for x in str(n)])
        if n in cache:
            result ^= cache[n]
            break
    cache[original] = result
    return result

def solution():
    return len([x for x in xrange(1,1000000) if len(chain(x)) == 60])

if __name__ == "__main__":
    print solution()
