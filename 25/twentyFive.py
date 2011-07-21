#!/usr/bin/env python

previousNum = 0
currentNum = 1
def nextFib():
  global previousNum
  global currentNum
  
  # temp = previousNum
  # previousNum = currentNum
  currentNum += previousNum
  previousNum = currentNum - previousNum
  
  return previousNum
  
seqNum = 1
while( len(str(nextFib())) < 1000 ):
  seqNum += 1

print seqNum