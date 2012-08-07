#!/usr/bin/env python
#
# Project Euler 92

ends_at_89 = set([89])
ends_at_1  = set([1])
def arrives_at_89(n):
    while True:
        next = sum([int(x)**2 for x in str(n)])
        if next in ends_at_89:
            ends_at_89.add(n)
            return True
        if next in ends_at_1:
            ends_at_1.add(n)
            return False
        n = next
        
def solution():
    return len([x for x in xrange(1,10000000) if arrives_at_89(x)])

if __name__ == "__main__":
    print solution()
