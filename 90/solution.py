#!/usr/bin/env python
#
# Project Euler 90

from itertools import product


squares = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), 
           (3, 6), (4, 6), (6, 4), (8, 1)]


def makes_square_numbers(die1, die2):
    die1 = [x if x != 9 else 6 for x in die1]
    die2 = [x if x != 9 else 6 for x in die2]
    for (a, b) in squares:
        if not ((a in die1 and b in die2) or (a in die2 and b in die1)):
            return False
    return True


def generate_distinct_arrangements():
    result = list()
    for a in xrange(0, 5):
        for b in xrange(a + 1, 6):
            for c in xrange(b + 1, 7):
                for d in xrange(c + 1, 8):
                    for e in xrange(d + 1, 9):
                        for f in xrange(e + 1, 10):
                            result.append((a, b, c, d, e, f))
    return result

def solution():
    result = 0
    distinct_arrangements = generate_distinct_arrangements()
    for i in xrange(len(distinct_arrangements)):
        for j in xrange(i+1, len(distinct_arrangements)): 
            if makes_square_numbers(distinct_arrangements[i], 
                                    distinct_arrangements[j]):
                result +=1
    return result


if __name__ == "__main__":
    print solution()
