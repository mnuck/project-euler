#!/usr/bin/env python

def isPalindrome(n):
  s = str(n)
  retval = True
  for i in xrange(len(s)/2):
    if(s[i] != s[-(i+1)]):
      retval = False
      break
  return retval

maxPalindrome = 0
for x in xrange(100,1000):
  for y in xrange(100, 1000):
    product = x * y
    if( isPalindrome(product) ):
      if( product > maxPalindrome ):
        maxPalindrome = product
print maxPalindrome
