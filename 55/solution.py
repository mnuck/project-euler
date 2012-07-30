#!/usr/bin/env python

def reverse_an_integer(n):
  """Reverse the order of digits in an integer"""
  return int(''.join(reversed(str(n))))

def is_palindrome(n):
  """Returns true if n is a palindromic number, false otherwise"""
  return reverse_an_integer(n) == n

def lychrel(n):
  """Returns true if n is probably a Lychrel number, false otherwise"""
  for i in xrange(50):
    n += reverse_an_integer(n)
    if is_palindrome(n):
      return False
  return True

def solution():
  """Returns the number of positive integers below 10k
     that are probably Lychrel numbers"""
  return len(filter(lychrel, xrange(1,10001)))

if __name__ == "__main__":
  print solution()
