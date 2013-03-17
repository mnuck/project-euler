#!/usr/bin/env python
#
# Project Euler 77

from collections import defaultdict
from math import sqrt


def isPrime(n):
    trial = 2
    primality = True
    while trial <= sqrt(n):
        if n % trial == 0:
            primality = False
            break
        else:
            trial += 1
    return primality


primes = [2, 3]
i = 4

while primes[-1] < 10000:
    i += 1
    if isPrime(i):
        primes.append(i)


max_to_check = 75
coins = [x for x in primes if x <= max_to_check]

result = defaultdict(int)

closed = set()
valid = set()

goal = 75

frontier = list()
frontier.append(tuple([0] * len(coins)))
while frontier:
    current = frontier.pop()
    for i in xrange(len(current)):
        child = list(current)
        child[i] += 1
        child = tuple(child)
        if tuple(child) in closed:
            continue
        closed.add(child)
        total = sum(x * y for (x, y) in zip(child, coins))
        if total <= goal:
            frontier.append(child)
            if sum(child) > 1:
                result[total] += 1


possibles = list()
for (k, v) in result.items():
    if v > 5000:
        possibles.append(k)

print min(possibles)
