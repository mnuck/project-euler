#!/usr/bin/env python
#
# Project Euler 53
#
# With 1 <= n <= 100, 
#      1 <= r <= n, how many values of combo_count > one million?

import operator

def product(xl):
    return reduce(operator.__mul__, xl, 1)


def combo_count(n,r):
    return  product(range(1,n+1)[r:]) / \
            product(range(1,n-r+1))
    

count = 0
for n in xrange(1, 101):
    for r in xrange(1, n):
        if combo_count(n,r) > 1000000:
            count += 1
print count
    
