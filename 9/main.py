#!/usr/bin/env python

from math import sqrt

for b in xrange(1,1000):
  for a in xrange(1,b):
    c = sqrt( a*a + b*b )
    if( c == int(c) ):
      if( a+b+int(c) == 1000 ):
        print a,b,int(c), a*b*int(c)