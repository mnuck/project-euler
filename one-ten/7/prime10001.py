#!/usr/bin/env python

from math import sqrt

def isPrime(n):
  trial = 2
  primality = True
  while( trial <= sqrt(n) ):
    if( n % trial == 0 ):
      primality = False
      break
    else:
      trial += 1
  return primality  


primes = [2,3]
i = 4

while( len(primes) < 10001 ):
  i += 1
  if( isPrime(i) ):
    primes.append(i)
    print len(primes), i
