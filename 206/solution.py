#/usr/bin/env python
#
# Project Euler 206

'''
1_2_3_4_5_6_7_8_9_0
'''

# all finders work by expanding binary search
# f returns -1 if too low, 1 if too high, 0 if in range

def lower_bound_satisfying(f, lower=1, upper=1):
    "finds the lowest n such that f(n) returns 0"
    while f(upper) == -1:
        lower = upper
        upper = upper * 2

    outer_lower = lower
    assert(f(outer_lower) == -1)

    halfway = (lower + upper) / 2
    while f(halfway) != 0:
        if f(halfway) == -1:
            lower = halfway
        else:  # f(halfway) == 1
            upper = halfway
        halfway = (lower + upper) / 2

    assert(f(halfway) == 0)
    lower = outer_lower

    while upper - lower > 1:
        halfway = (lower + upper) / 2
        if f(halfway) == -1:
            lower = halfway
        else:
            upper = halfway
        if halfway - lower == 1:
            upper = halfway
            break
    return upper


def upper_bound_satisfying(f, lower=1, upper=1):
    "finds the lowest n such that f(n) returns 0"
    while f(upper) != 1:
        lower = upper
        upper = upper * 2

    outer_upper = upper
    assert(f(outer_upper) == 1)

    halfway = (lower + upper) / 2
    while f(halfway) != 0:
        if f(halfway) == -1:
            lower = halfway
        else:  # f(halfway) == 1
            upper = halfway
        halfway = (lower + upper) / 2

    assert(f(halfway) == 0)
    upper = outer_upper

    while upper - lower > 1:
        halfway = (lower + upper) / 2
        if f(halfway) == 1:
            upper = halfway
        else:
            lower = halfway
        if upper - halfway == 1:
            upper = halfway
            break
    return lower

def valid(x):
    s = str(x)
    if len(s) != 19:
        return False
    if s[0] != "1":
        return False
    if s[2] != "2":
        return False
    if s[4] != "3":
        return False
    if s[6] != "4":
        return False
    if s[8] != "5":
        return False
    if s[10] != "6":
        return False
    if s[12] != "7":
        return False
    if s[14] != "8":
        return False
    if s[16] != "9":
        return False
    if s[18] != "0":
        return False
    return True

def solution():
    def f(x):
        x = x * x
        if x > 1929394959697989990:
            return 1
        if x < 1020304050607080900:
            return -1
        return 0

    lower = lower_bound_satisfying(f)
    upper = upper_bound_satisfying(f)

    for i in xrange(lower, upper):
        if valid(i*i):
            return i
    return None


if __name__ == "__main__":
    print solution()
