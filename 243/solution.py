#!/usr/bin/env python                                                                                                                              

from fractions import Fraction

def totient(n):
  return 1

def solution():
  goal = Fraction(15499, 94744)
  d = 2
  while Fraction(totient(d), d) >= goal:
    d += 1
  return d

if __name__ == "__main__":
  print solution()
