#!/usr/bin/env python

closed = set()
rewrite = {
  '10': '02',
  '20': '12'
}

def process(input):
  if input in closed:
    return 0
  result = 1
  closed.add(input)
  for i in xrange(len(input)-1):
    lhs = input[i:i+2]
    if lhs in rewrite:
      result += process(input[:i] + rewrite[lhs] + input[i+2:])
  return result
  
def solution(n):
  return process(bin(n)[2:])

def fast_solution(n):
  groups = bin(n)[2:].split('1')
  steps = [1]
  results = steps[-1]
  for group in groups[1:]:
    result = steps[-1] + len(group) * sum(steps)
    steps.append(result)
  return result

if __name__ == "__main__":
  print fast_solution(10**25)
