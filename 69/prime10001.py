#!/usr/bin/env python

from math import sqrt

def isPrime(n):
  trial = 2
  while( trial <= sqrt(n) ):
    if( n % trial == 0 ):
      return False
    else:
      trial += 1
  return True

print 2
print 3
for i in xrange(4,1000001):
  if( isPrime(i) ):
    print i
