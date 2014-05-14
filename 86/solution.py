#!/usr/bin/env python
#
# Project Euler 87

'''
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3,
and a fly, F, sits in the opposite corner. By travelling on the surfaces
of the room the shortest "straight line" distance from S to F is 10 and
the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given
cuboid and the shortest route doesn't always have integer length.

By considering all cuboid rooms with integer dimensions, up to a maximum
size of M by M by M, there are exactly 2060 cuboids for which the shortest
route has integer length when M=100, and this is the least value of M for
which the number of solutions first exceeds two thousand; the number of
solutions is 1975 when M=99.

Find the least value of M such that the number of solutions first exceeds
one million.
'''

def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def is_square(n):
    sqrt_n = isqrt(n)
    return n == sqrt_n * sqrt_n


def shortest_is_integral(a, b, c):
    u = b + c
    v = a + c
    w = a + b
    p1 = a * a + u * u
    p2 = b * b + v * v
    p3 = c * c + w * w
    path = min(p1, p2, p3)
    return is_square(path)


cuboid_cache = {0: 0}

def cuboids_underX(m):
    if (m - 1) not in cuboid_cache:
        cuboids_under(m-1)
    result = cuboid_cache[m-1]
    a = m
    for b in xrange(1, m + 1):
        for c in xrange(b, m + 1):
            if shortest_is_integral(a, b, c):
                result += 1
    cuboid_cache[m] = result
    return result

def cuboids_underY(m):
    result = 0
    for a in xrange(1, m + 1):
        for b in xrange(a, m + 1):
            for c in xrange(b, m + 1):
                if shortest_is_integral(a, b, c):
                    result += 1
    return result

cuboids_under = cuboids_underX

def solution():
    M = 1
    solutions = cuboids_under(M)
    while solutions < 1000000:
        M += 1
        solutions = cuboids_under(M)
        print M, solutions
    return M

if __name__ == "__main__":
    print solution()
