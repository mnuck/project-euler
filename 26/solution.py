#!/usr/bin/env python

# Find the value of d < 1000 for which 1/d contains the longest recurring 
# cycle in its decimal fraction part.

def findRepeating(n):
    searchString = str( (10 **(2*n - 1) / n ))
    result = 0
    for x in xrange(1,n):
        if( searchString[:2*x].count(searchString[:x-1]) == 2 ):
            return x + 1
    return result

maxRepeating = 0
for n in xrange(1000,1,-1):
  repeating = findRepeating(n)
  if repeating > maxRepeating:
      maxRepeating = repeating
      print n, "repeats after ", repeating, "digits"
      print str( (10 ** (2*n - 1) / n ))
      
