#!/usr/bin/env python

from math import sqrt

primes = set([2,3])
def isPrime(n):
  for prime in (x for x in primes if x <= sqrt(n)):
    if n % prime == 0:
      return False
  primes.add(n)
  return True

def prime_factors(n):
  """Depends on the primes set being properly loaded"""
  result = set()
  while n > 1:
    for prime in primes:
      while n % prime == 0:
        result.add(prime)
        n /= prime
  return result
    

def solution():
  magic = 4
  n = 4
  count = 0
  while True:
    if n % 1000 == 0:
      print n
    n += 1
    isPrime(n)
    f_count = len(prime_factors(n))
    if f_count == magic:
      count += 1
    else:
      count = 0
    if count == magic:
      return n - count + 1


if __name__ == "__main__":
  print "SOLUTION: %i" % solution()
