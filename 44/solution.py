#!/usr/bin/env python

def pentagonal(n):
  return (3*n - 1) * n / 2


def solution():
  plist = list()
  pset  = set()
  n = 0
  while True:
    n += 1
    d = pentagonal(n)
    for a in plist:
      print d, a
      b = d - a
      if b in pset:
        c = a - b
        if c in pset:
          return c
    plist.append(d)
    pset.add(d)

if __name__ == "__main__":
  print solution()

