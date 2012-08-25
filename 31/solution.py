# -*- coding: latin-1 -*-
# Project Euler 31
#
# In England the currency is made up of pound, £, and pence, p,
# and there are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
# 1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
# How many different ways can £2 be made using any number of coins?

coins = [200, 100, 50, 20, 10, 5, 2, 1]
closed = set()
valid = set()

goal = 200

frontier = list()
frontier.append(tuple([0,0,0,0,0,0,0,0]))
while frontier:
    current = frontier.pop()
    for i in xrange(len(current)):
        child = list(current)
        child[i] += 1
        child = tuple(child)
        if tuple(child) in closed:
            continue
        closed.add(child)
        total = sum(x*y for (x,y) in zip(child,coins))
        if total == goal:
            #print child
            valid.add(child)
        elif total < goal:
            frontier.append(child)
        
print len(list(valid))

