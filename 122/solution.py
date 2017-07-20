#!/usr/bin/env python

import sys

goal = 0
goal_depth = 0

def backtrack(path):
  global goal_depth
  current = path[0]
  current_depth = len(path) - 1
  if current > goal:
    return False
  if current == goal:
    goal_depth = current_depth
    return True
  if current_depth == goal_depth - 1:
    return True
  for step in path:
    if backtrack([current + step] + path):
      return False
  return False

def m(k):
  global goal_depth
  global goal
  goal = k
  goal_depth = sys.maxint
  backtrack([1])
  return goal_depth

def solution():
  return sum(m(k) for k in xrange(1, 201))

if __name__ == "__main__":
  print solution()
