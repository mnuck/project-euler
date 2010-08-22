#!/usr/bin/env python

cheat = dict()

def chainLen(n):
  startN = n
  len = 1
  while(n != 1):
    if(n%2 == 0):
      n = n/2
    else:
      n = 3*n + 1
    if(n in cheat):
      len += cheat[n]
      break
    len += 1
  cheat[startN] = len
  return len
  
maxLen = 1  
for n in xrange(1,1000000):
  l = chainLen(n)
  if(l > maxLen):
    maxLen = l
    print n, maxLen