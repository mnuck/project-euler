#!/usr/bin/env python

from math import sqrt

primes = [2,3]
squares = [1,4]

def isPrime(n):
  trial = 2
  primality = True
  while( trial <= sqrt(n) ):
    if( n % trial == 0 ):
      primality = False
      break
    else:
      trial += 1
  if primality:
    primes.append(n)
  return primality


def solution():
  n = 7
  while True:
    n += 2
    if not isPrime(n):
      for prime in primes:
        m = n - prime
        if isSquare(m):
          break
      return n

if __name__ == "__main__":
  print solution()
