#!/usr/bin/env python
#
# Project Euler 94

# a^2 + b^2 = c^2
# c^2 - b^2 = a^2

from math import sqrt
def is_square(n):
    m = int(sqrt(n))
    return n == m * m

def is_valid(c,a):
    return is_square(c*c - a*a)

def high(c):
    return is_valid(c, c/2 + 1)

def low(c):
    return is_valid(c, c/2)

def both(c):
    if is_valid(c, c/2):
        print c, "low!"
    if is_valid(c, c/2 + 1):
        print c, "high!"
        
def solution():    
    return "buttes"

#if __name__ == "__main__":
#    print solution()

"""
find a "base" of the form n = k^2 + 1 where k is even and n is valid high
each "base" adds 3*n + 1 perimeter to the total

between each n_i and n_i+1 there exists m = k_i*k_i+1 + 1
for each halfway number m, add 3*m - 1 perimeter to the total
"""

perimeter = 0

bases = [c for c in xrange(2,25000,2) if high(c*c+1)]
for base in bases:
    n = base*base + 1
    p = 3*n + 1
    if p < 1000000000:
#        print n, "used", p
        perimeter += p

for i in xrange(1,len(bases)):
    m = bases[i]*bases[i-1] + 1
    p = m*3 - 1
    if p < 1000000000:
#        print m, "used", p
        perimeter += p

print perimeter
