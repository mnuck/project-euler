#!/usr/bin/env python

from math import sqrt

def reverse_an_integer(n):
  return int(''.join(reversed(str(n))))

def is_palindrome(n):
  return reverse_an_integer(n) == n

def sum_first_n_squares(n):
  if n == 0:
    return 0
  return n * (n + 1) * (2*n + 1) / 6

def solution(n):
  top = int(sqrt(n))
  found = set()
  for i in xrange(1, top + 1):
    for j in xrange(0, i - 1):
      a = sum_first_n_squares(i) - sum_first_n_squares(j)
      if a < n and is_palindrome(a) and not a in found:
        found.add(a)
  return sum(x for x in found)

if __name__ == "__main__":
  print solution(pow(10, 8))
