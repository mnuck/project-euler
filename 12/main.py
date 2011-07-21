#!/usr/bin/env python

def numFactors(n):
  factors = 2
  for i in xrange( 2, (n/2)+1 ):
    if( n % i == 0 ):
      factors += 1
  return factors

i = 1
biggest_n = 0
triangle = i
while( True ):
  i += 1
  triangle += i
  n = numFactors(triangle)
  if( n > biggest_n ):
    biggest_n = n
    print triangle, n
  if(n > 500):
    break
