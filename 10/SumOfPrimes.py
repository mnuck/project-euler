#!/usr/bin/env python
# Sieve of E

n = 2000000

a = [True] * n
i = 2
while( i < n/2 ):
  for j in xrange( 2*i, n, i ):
    a[j] = False
  i += 1
  while( not a[i] ):
    i += 1

total = 0
for i in xrange(2,n):
  if( a[i] ):
    total += i
    
print total



