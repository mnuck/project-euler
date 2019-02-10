#!/usr/bin/env python

import math

def score(n, turns): # n is a number
  '''returns the product of the probability numerators'''
  result = 1
  for i in xrange(turns):
    if n % 2 == 0:
      result *= (i + 1)
    n /= 2
  return result

def solution(turns):
  threshold = math.floor(turns/2) + 1;
  numerator = 0
  for i in xrange(0, 2**turns):
    count = bin(i).count("1")
    if (count >= threshold):
      numerator += score(i, turns)

  denominator = math.factorial(turns + 1);

  return  math.floor(denominator / numerator)

if __name__ == "__main__":
  print solution(15)
