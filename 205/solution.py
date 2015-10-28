#!/usr/bin/env python
#
# Project Euler 205

"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins.
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin?
Give your answer rounded to seven decimal places in the form 0.abcdefg
"""

import itertools

def rollHistogram(n, sides):
    result = [0] * ((n * sides) + 1)
    die = range(1, sides + 1)
    for roll in itertools.product(die, repeat=n):
        result[sum(roll)] += 1
    return result

def solution():
    peter = rollHistogram(9, 4)
    colin = rollHistogram(6, 6)

    peterSum = sum(peter)
    colinSum = sum(colin)

    peter = [x * colinSum for x in peter]
    colin = [x * peterSum for x in colin]

    colinLessThan = [sum(colin[:i]) for i, _ in enumerate(colin)]
    products = [x*y for x,y in zip(peter, colinLessThan)]
    denominator = peterSum * peterSum * colinSum * colinSum

    return round(float(sum(products)) / denominator, 7)


if __name__ == "__main__":
    print solution()
