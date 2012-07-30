#!/usr/bin/env python

def are_permutations(a, b):
  return sorted(str(a)) == sorted(str(b))

def check_validity(n):
  return are_permutations( n*2, n*3 ) \
     and are_permutations( n*3, n*4 ) \
     and are_permutations( n*4, n*5 ) \
     and are_permutations( n*5, n*6 )

def main(n):
  while not check_validity(n):
    n += 1
  print n

if __name__ == "__main__":
    main(1)
