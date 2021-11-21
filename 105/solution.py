#!/usr/bin/env python
import sys, os
sys.path.append(os.path.realpath('..'))
from eulerlib.special_sum_set import special_sum_set

def solution():
    result = 0
    with open("sets.txt") as file:
        for line in file:
            s = [int(x) for x in line.split(",")]
            if special_sum_set(s):
                result += sum(s)
    return result

if __name__ == "__main__":
    print(solution())
