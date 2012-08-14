#!/usr/bin/env python
#
# Project Euler 63

"""
n**p

This problem exists, so the answer is not infinity. So.

For each positive integer n where n < N, where N is an unknown upper bound,
there exist p1 and p2 such that:
compare(n,p1-1) == -1
compare(n,p1) == 0   # so p1 is the lower bound
compare(n,p2) == 0
compare(n,p2+1) == 1 # so p2 is the upper bound

For each positive integer p where p < P where P in an unknown upper bound,
there exist n1 and n2 such that:
compare(n1-1,p) == -1
compare(n1,p) == 0 # so n1 is the lower bound
compare(n2,p) == 0
compare(n2+1,p) == 1 # so n2 is the upper bound
"""

def compare(n, p):
    return cmp(len(str(n**p)), p)

def lower(p):
    result = 1
    while compare(result,p) == -1:
        result += 1
    if compare(result,p) == 1:
        return False
    return result

def upper(p):
    result = lower(p)
    if not result:
        return False
    while compare(result,p) == 0:
        result += 1
    return result - 1

def bandwidth(p):
    if lower(p):
        return upper(p) - lower(p) + 1
    return 0

def solution():
    result = 0
    n = 1
    while lower(n):
        result += bandwidth(n)
        n += 1
    return result

if __name__ == "__main__":
    print solution()
