#!/usr/bin/env python
#
# Project Euler 84

from itertools import product
sides = 4
denom = float(sides * sides)


def modal_string(weights):
    result = list(enumerate(weights))
    result.sort(key=lambda (x, y): y, reverse=True)
    print result
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

    # go to jail (tweeeeeet)
    result[10] += result[30]
    result[30] = 0.0

    # CC1
    result[0] += result[2] * (1.0 / 16)
    result[10] += result[2] * (1.0 / 16)
    result[2] *= (1 - (2.0 / 16))

    # CC2
    result[0] += result[17] * (1.0 / 16)
    result[10] += result[17] * (1.0 / 16)
    result[17] *= (1 - (2.0 / 16))

    # CC3
    result[0] += result[33] * (1.0 / 16)
    result[10] += result[33] * (1.0 / 16)
    result[33] *= (1 - (2.0 / 16))

    # CH1
    result[0] += result[7] * (1.0 / 16)
    result[10] += result[7] * (1.0 / 16)
    result[11] += result[7] * (1.0 / 16)
    result[24] += result[7] * (1.0 / 16)
    result[39] += result[7] * (1.0 / 16)
    result[5] += result[7] * (1.0 / 16)
    result[15] += result[7] * (2.0 / 16)
    result[12] += result[7] * (1.0 / 16)
    result[4] += result[7] * (1.0 / 16)
    result[7] *= (1 - (10.0 / 16))

    # CH2
    result[0] += result[22] * (1.0 / 16)
    result[10] += result[22] * (1.0 / 16)
    result[11] += result[22] * (1.0 / 16)
    result[24] += result[22] * (1.0 / 16)
    result[39] += result[22] * (1.0 / 16)
    result[5] += result[22] * (1.0 / 16)
    result[25] += result[22] * (2.0 / 16)
    result[28] += result[22] * (1.0 / 16)
    result[19] += result[22] * (1.0 / 16)
    result[22] *= (1 - (10.0 / 16))

    # CH3
    result[0] += result[36] * (1.0 / 16)
    result[10] += result[36] * (1.0 / 16)
    result[11] += result[36] * (1.0 / 16)
    result[24] += result[36] * (1.0 / 16)
    result[39] += result[36] * (1.0 / 16)
    result[5] += result[36] * (1.0 / 16)
    result[5] += result[36] * (2.0 / 16)
    result[12] += result[36] * (1.0 / 16)
    result[33] += result[36] * (1.0 / 16)
    result[36] *= (1 - (10.0 / 16))

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
