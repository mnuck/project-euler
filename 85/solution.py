#!/usr/bin/env python
#
# Project Euler 87

'''
By counting carefully it can be seen that a rectangular grid measuring
3 by 2 contains eighteen rectangles. Although there exists no rectangular
grid that contains exactly two million rectangles, find the area of the grid
with the nearest solution.
'''

from itertools import product

closest_rectangles = 0
def is_closest(i, j):
    global closest_rectangles
    rectangles = num_of_rectangles(i, j)
    if abs(2000000 - rectangles) < abs(2000000 - closest_rectangles):
        closest_rectangles = rectangles
        return True
    return False


#def num_of_rectangles(x, y):
#    return sum((i + 1) * (j + 1) for (i, j)
#               in product(xrange(x), xrange(y)))


def num_of_rectangles(x, y):
    return x * (x + 1) * y * (y + 1) / 4

def solution():
    for i in xrange(1, 80):
        for j in xrange(1, i+1):
            if is_closest(i, j):
                best_i, best_j = i, j
    return best_i * best_j


if __name__ == "__main__":
    print solution()
