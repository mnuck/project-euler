#!/usr/bin/env python
#
# Project Euler 61

from itertools import permutations

def triangle(n):   return n * (n + 1) / 2
def square(n):     return n * n
def pentagonal(n): return n * (3*n - 1) / 2
def hexagonal(n):  return n * (2*n - 1)
def heptagonal(n): return n * (5*n - 3) / 2
def octagonal(n):  return n * (3*n - 2)


def make_4digits(f):
    result = list()
    base = 0
    n = f(base)
    while n < 10000:
        if n > 999:
            result.append(n)
        base += 1
        n = f(base)
    return result


def make_table(numbers):
    result = dict()
    for n in numbers:
        key = str(n)[:2]
        value = str(n)[2:]
        if key not in result:
            result[key] = list()
        result[key].append(value)
    return result


def score(seq):
    result = 0
    for i in xrange(0,len(seq) - 1):
        result += int(seq[i] + seq[i+1])
    result += int(seq[-1] + seq[0])
    return result


def partial(working, current, tables):
    next = (current + 1) % len(tables)
    key = working[-1]
    if key not in tables[next]:
        return False
    if len(working) == len(tables):
        if working[0] in tables[next][key]:
            return working
        else:
            return False
    for value in tables[next][key]:
        next_attempt = list(working)
        next_attempt.append(value)
        result = partial(next_attempt, next, tables)
        if result:
            return result
    return False


def solution():
    master_tables = [make_table(make_4digits(f))
                     for f in (triangle, square, pentagonal,
                               hexagonal, heptagonal, octagonal)]
    for table in permutations(master_tables):
        for key in table[0]:
            result = partial([key], -1, table)
            if result:
                return score(result)

            
if __name__ == "__main__":
    print solution()
