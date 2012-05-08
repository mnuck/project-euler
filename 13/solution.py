#!/usr/bin/env python
#
# Project Euler 13
#
# First ten digits of the sum of some big numbers

with open('numbers.txt', 'r') as f:
    print str(sum(int(x) for x in f.readlines()))[:10]
