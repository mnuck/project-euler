#!/usr/bin/env python

from math import sqrt

smallPrimes = set([2, 3, 5])
def isPrime( x ):
    global smallPrimes
    if( x < 2 ):
        return False
    for p in [i for i in smallPrimes if i*i <= x]:
        if( x % p == 0 ):
            return False
    biggestKnown = max(smallPrimes)
    if( biggestKnown * biggestKnown > x ):
        smallPrimes.add(x)
        return True
    else:
        for p in xrange(biggestKnown, int(sqrt(x))):
            if( x % p == 0 ):
                return False
        return True

a = [x for x in xrange(10000) if isPrime(x)]
smallPrimes = set(a)

def howMany(a, b):
    n = 0
    while( isPrime(n**2 + a*n + b) ):
        n += 1
    return n

maxN = 0
maxA = 0
maxB = 0
for b in [x for x in smallPrimes if x < 1000]:
    for a in xrange(-1000,1001):
        n = howMany(a, b)
        if( n > maxN ):
            maxN = n
            maxA = a
            maxB = b
            print a,b,n
print maxA * maxB
