#!/usr/bin/env python

from math import sqrt

primes = set([2,3])
def isPrime(n):
  for prime in (x for x in primes if x <= sqrt(n)):
    if n % prime == 0:
      return False
  primes.add(n)
  return True

def isTwiceSquare(n):
  return not sqrt(n/2.0) % 1

def solution():
  n = 3
  while True:
    n += 2
    if not isPrime(n):
      winner = True
      for prime in primes:
        if isTwiceSquare(n - prime):
          winner = False
          break
      if winner:
        return n

if __name__ == "__main__":
  print solution()
