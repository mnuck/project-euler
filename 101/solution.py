#!/usr/bin/env python

from fractions import Fraction


def u(n):
  return (1 - n + pow(n, 2)
          - pow(n, 3) + pow(n, 4)
          - pow(n, 5) + pow(n, 6)
          - pow(n, 7) + pow(n, 8)
          - pow(n, 9) + pow(n, 10))


def OP(k, x):
  if k == 1:
    return u(1)
  result = Fraction(0, 1)
  for i in xrange(1, k + 1):
    subtotal = Fraction(u(i), 1)
    for j in xrange(1, k + 1):
      if i != j:
        subtotal *= Fraction(x - j, i - j)
    result += subtotal
  return result.numerator


def solution():
  result = 0
  for i in xrange(1, 11):
    j = 1
    while OP(i, j) == u(j):
      j += 1
    result += OP(i, j)
  return result


def main():
  print solution()


if __name__ == "__main__":
  main()
