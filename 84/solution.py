#!/usr/bin/env python
#
# Project Euler 84

from itertools import product
sides = 4
denom = float(sides * sides)


def modal_string(weights):
    result = list(enumerate(weights))
    result.sort(key=lambda (x, y): y, reverse=True)
    result = [a for (a, b) in result]
    return "%.2d%.2d%.2d" % tuple(result[:3])


def dice_distribution(start):
    result = [0] * 40
    for (a, b) in product(xrange(1, sides + 1), xrange(1, sides + 1)):
        total = a + b
        result[total] += 1 / denom
        if a == b:
            result[total] *= (1 - (1 / (denom * 2)))  # DAFUQ
    result = result[40 - start:] + result[:40 - start]
    return result


def next_weights(nodes, edges):
    result = [0] * 40
    for (i, j) in product(xrange(40), xrange(40)):
        result[i] += nodes[j] * edges[j][i]

    # 3 doubles in a row
    result[10] += float(1) / (sides * sides * sides)

    def alter(source, targets):
        unit = result[source] * (1.0 / 16)
        result[source] -= unit * len(targets)
        for i in targets:
            result[i] += unit

    alter(30, [10] * 16)  # go to jail (tweeeeeet)
    alter(2, [0, 10])  # CC1
    alter(17, [0, 10])  # CC2
    alter(33, [0, 10])  # CC3
    alter(7, [0, 10, 11, 24, 39, 5, 15, 15, 12, 4])  # CH1
    alter(22, [0, 10, 11, 24, 39, 5, 25, 25, 28, 19])  # CH2
    alter(36, [0, 10, 11, 24, 39, 5, 5, 5, 12, 33])  # CH3

    return result


def main():
    weights = ([0] * 40)
    edge_matrix = [dice_distribution(i) for i in xrange(40)]
    weights[0] = 1.0
    for _ in xrange(10000):
        weights = next_weights(weights, edge_matrix)
    return modal_string(weights)


if __name__ == "__main__":
    print main()
