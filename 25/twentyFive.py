#!/usr/bin/env python

def nextFib():
  previous, current = 0, 1
  while True:
    yield previous
    previous, current = current, current + previous


solution, _ = ((term,value) for (term,value) 
               in enumerate(nextFib())
               if len(str(value)) >= 1000).next()

print solution
