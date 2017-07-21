#!/usr/bin/env python

from fractions import Fraction
from itertools import combinations

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def resilience(factors):
  n = 1
  totient = 1
  for factor in factors:
    n *= factor
    totient *= (factor - 1)
  return n, Fraction(totient, n - 1), totient / float(n - 1)

def solution():
  global primes
  goal = Fraction(15499, 94744)
  minD = 6469693231 # product of all primes p where p < 30, plus 1
  for size in xrange(1, len(primes) + 1):
    for subset in combinations(primes, size):
      d, r, f = resilience(list(subset))
      print d, r, f, list(subset)
      if r < goal and d < minD:
        minD = d
        print "new solution:", d, r
    print
  return minD

minD = solution()
print minD

def totient(factors):
    result = 1
    for prime, exponent in factors:
        result *= (prime - 1)
        if exponent > 1:
            result *= pow(prime, (exponent - 1))
    return result
  
def f(factors):
  global minD
  goal = Fraction(15499, 94744)
  t = totient(factors)
  d = 1
  for prime, exponent in factors:
    d *= pow(prime, exponent)
  print d, t / float(d - 1), factors
  if Fraction(t, d-1) < goal:
    if d < minD:
      minD = d
      print "new solution:", d 

f([(2, 1), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1), (23, 1), (29, 1)])
f([(2, 1), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1), (23, 1)])
f([(2, 2), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1), (23, 1)])
f([(2, 3), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1), (23, 1)])
f([(2, 4), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1), (23, 1)])

print minD
