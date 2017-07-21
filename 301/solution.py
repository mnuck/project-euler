#!/usr/bin/env python

print sum(1 for n in xrange(1, pow(2, 30) + 1) if n ^ (2*n) ^ (3*n) == 0)
