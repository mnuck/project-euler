#!/usr/bin/env python
#
# Project Euler 56

from itertools import product

def digital_sum(n):
    return sum([int(x) for x in str(n)])

def solution():
    return max([digital_sum(a**b)
                for (a,b) in product(xrange(1,100), 
                                     xrange(1,100))])

if __name__ == "__main__":
    print solution()
