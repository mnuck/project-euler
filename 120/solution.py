#!/usr/bin/env python

def solution():
  result = 0
  for i in xrange(3, 1001):
    result += 2*i*((i-1)/2) # on purpose to correctly capture both evens and odds
  return result

if __name__ == "__main__":
  print solution()
