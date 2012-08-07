#!/usr/bin/env python

def pentagonal(n):
  return (3*n - 1) * n / 2

def solution():
  pents = set()
  n = 0
  while True:
    n += 1
    d = pentagonal(n)
    for a in pents:
      b = d - a
      if b in pents:
        c = a - b
        if c in pents:
          return c
    pents.add(d)

if __name__ == "__main__":
  print solution()

