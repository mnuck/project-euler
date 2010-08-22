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


a = 600851475143

divisor = 2

while( a > 1 ):
  while( not isPrime(divisor)):
    divisor += 1
  while( a % divisor == 0 ):
    print divisor, a
    a /= divisor
  divisor += 1
