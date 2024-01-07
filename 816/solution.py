#!/usr/bin/env python
#
# Project Euler 816
#
# mnuck@zephyr 816 % time python3 solution.py
# 20.8806130178211
# python3 solution.py  2.12s user 0.08s system 98% cpu 2.243 total
# 2.12 seconds on a Macbook Air M1 2020

from math import sqrt


# this prng loops at iteration 6,308,950 with 629527
# which doesn't help with this problem because we're only using 4,000,000
# but is always good to check because hey, maybe it loops early
s = 290797
def prng():
    global s
    x = s
    s = pow(s, 2, 50515093)
    return x


def generate_numbers(n):
    result = []
    for i in range(n):
        result.append(prng())
    return result


def generate_points(numbers):
    result = []
    for i in range(len(numbers) // 2):
        result.append((numbers[2*i], numbers[2*i + 1]))
    return result


def solution(n):
    numbers = generate_numbers(2 * n)
    points = generate_points(numbers)

    # sort the points ascending on the x coordinate
    # this is the key optimization
    points.sort(key = lambda x: x[0])

    # the set of natural numbers is closed over pow and mod
    # therefore the prng can never give us a negative or a fraction
    # therefore the smallest distance between two distinct points is >= 1.
    # therefore we can drop the sqrt from the hypotenuse calculation.
    #  it's expensive, and the pair of points with the shortest distance
    #  is also going to be the pair of points with the shortest pow(distance, 2).

    # c_squared = a_squared + b_squared
    #  so if either a_squared or b_suqared is bigger than our known min_dist_squared
    #  we can bail out early on that iteration and not calculate the other:
    #  we're already too big.
    #  in fact, since we're sorted on the x coordinate, we can bail out on that p1
    #  entirely, because every p2 after is guaranteed to be even further away.
    min_dist_squared = 99999999999999999999999999999999
    for i in range(len(points) - 1):
        p1 = points[i]
        for j in range(i+1, len(points)):
            p2 = points[j]
            a = p2[0] - p1[0]
            a_sq = a * a
            if a_sq > min_dist_squared:
                # too far in x, get me another p1
                break
            b = p2[1] - p1[1]
            b_sq = b * b
            if b_sq > min_dist_squared:
                # too far in y, get me another p2
                continue
            d_sq = a_sq + b_sq
            if d_sq < min_dist_squared:
                min_dist_squared = d_sq
    return sqrt(min_dist_squared)


if __name__ == "__main__":
    print(solution(2000000))
