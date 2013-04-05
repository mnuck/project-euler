#!/usr/bin/env python
# Euler 91
#
# Right Triangles

from itertools import product
bounds = 50


def main():
    count = 0
    seen = set()
    for (x1, x2, y1, y2) in product(xrange(bounds + 1),
                                    xrange(bounds + 1),
                                    xrange(bounds + 1),
                                    xrange(bounds + 1)):
        if (x1, x2, y1, y2) not in seen:
            count += 1 if is_right(x1, x2, y1, y2) else 0
            seen.add((x1, x2, y1, y2))
            seen.add((x2, x1, y2, y1))
    return count


def is_right(x1, x2, y1, y2):
    if x1 == 0 and y1 == 0:
        return False
    if x2 == 0 and y2 == 0:
        return False
    if x1 == x2 and y1 == y2:
        return False

    a2 = x1 ** 2 + y1 ** 2
    b2 = x2 ** 2 + y2 ** 2
    c2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
    leg1, leg2, hypotenuse = sorted([a2, b2, c2])
    result = leg1 + leg2 == hypotenuse
#    print leg1, leg2, hypotenuse, result
    return result

if __name__ == "__main__":
    print main()
