#!/usr/bin/env python

# Project Euler 144

import math

def pointsToLine(p1, p2):
    # input schema: {x, y}, {x, y}
    # output schema: ax + by = c, direction true if p2.x >= p1.x
    # ax_1 + by_1 = c
    # ax_2 + by_2 = c
    # ax_1 + by_1 = ax_2 + by_2
    # ax_1 - ax_2 = by_2 - by_1
    # a(x_1 - x_2) = b(y_2 - y_1)
    # a/b = (y_2 - y_1)/(x_1 - x_2)
    # b/a = (x_1 - x_2)/(y_2 - y_1)
    # b = a(x_1 - x_2)/(y_2 - y_1)
    if p1.x == p2.x: # vertical line, infinite slope
        return {a:1, b:0, c:p1.x, direction: True}
    a = 1
    b = (p1.x - p2.x) / (p2.y - p1.y)
    c = a * p1.x + b * p1.y
    return {a: a, b: b, c: c, direction: p2.x >= p1.x}

def exits(line):
    # input schema {a, b, c, direction} ax + by = c
    # gap at the top at -0.01 <= x <= 0.01
    # 4(0.01)(0.01) + y**2 = 100
    # 4(0.0001) + y**2 = 100
    # y**2 = 100 - 0.0004
    # y ~= 10
    y = math.sqrt(100 - 0.004)

    # ax + by = c
    # ax = c - by
    # x = (c - by)/a
    x = (line.c - line.b * y) / line.a
    if math.abs(x) <= 0.01:
        return True
    return False

def bounce(line):
    # ellipse defined by 4x**2 + 1y**2 = 100
    # ellipse slope m = -4x/y
    # normal line slope n = -y/4x
    # angle between incoming line and normal line equals angle between outgoing line and normal line
    return {a: 42.0, b: 4.2, c: 0.42, direction: 1}    

def solution():
    result = 1
    line = pointsToLine({x:0.0, y:10.0}, {x:1.4, y:-9.6})
    line = bounce(line);
    while not exits(line):
        line = bounce(line)
        result +=1
    return result

if __name__ == "__main__":
    print solution()
