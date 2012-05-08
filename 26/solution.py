#!/usr/bin/env python

# Find the value of d < 1000 for which 1/d contains the longest recurring 
# cycle in its decimal fraction part.

# not proud of this one, but it works

def findRepeating(n):
    searchString = str( (10 **(2*n - 1) / n ))
    result = n - 1
    for x in xrange(1,n+2):
        substr  = searchString[-x:]
        substr2 = searchString[-2*x:-x]
        if substr == substr2:
            return x
    return result


maxRepeating = 0
for n in xrange(999,1,-1):
  repeating = findRepeating(n)
  if repeating > maxRepeating:
      maxRepeating = repeating
      print n, "repeats after ", repeating, "digits"
      
