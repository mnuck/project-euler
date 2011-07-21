#!/usr/bin/env python

def pascalTriangle(n):
  """Return Pascal's Triangle down to depth n | n > 2"""
  a = list()
  a.append( [1] )
  a.append( [1, 1] )
  for depth in xrange(2, n):
    prevRow = a[-1]
    nextRow = list()
    nextRow.append(1)
    for i in xrange(depth - 1):
      nextRow.append(prevRow[i] + prevRow[i+1])
    nextRow.append(1)
    a.append(nextRow)
    
  return a

x = pascalTriangle(41)
print x[40][20]