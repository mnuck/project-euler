#!/usr/bin/env python
#
# Project Euler 62

from collections import Counter  # permutation finder

cubes = set()
base = 1
cube = base * base * base
while cube < 999999999999:
    cubes.add(cube)
    base += 1
    cube = base * base * base

def get_permutation_table():
    collider = dict()
    for number in cubes:
        key = tuple(dict(Counter(str(number))).items())
        if key not in collider:
            collider[key] = list()
        collider[key].append(number)
    return [x for x in collider.values() if len(x) > 4]

def candidates(s):
    maxlen = max(len(x) for x in s)
    return [min(x) for x in s if len(x) == maxlen]

def solution():
    return min(candidates(get_permutation_table()))

if __name__ == "__main__":
    print solution()
