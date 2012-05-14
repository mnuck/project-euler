#!/usr/bin/env python

def isPandigital(s):
    return sorted(list(s)) == ['1','2','3','4','5','6','7','8','9']
 
def generate(i):
    j = 1
    current = ""
    while len(current) < 9:
        current += str(i*j)
        j += 1
    return current

largest = 123456789

for i in xrange(1000000):
    x = generate(i)
    if isPandigital(x):
        if int(x) > largest:
            print x, i
            largest = int(x)
