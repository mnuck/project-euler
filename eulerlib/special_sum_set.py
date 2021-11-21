from math import ceil
from itertools import combinations

# Used in problems 103, 105, 106
#
# Let S(A) represent the sum of elements in set A of size n.
# We shall call it a special sum set if
# for any two non-empty disjoint subsets, B and C, the following properties are true:
# Property 1: S(B) != S(C); that is, sums of subsets cannot be equal.
# Property 2: If B contains more elements than C then S(B) > S(C).
#
# It also seems to be the case that elements must be positive integers.
# This is not stated in any of the problem statements, but all the
# examples assume this is true.

def special_sum_set(s_in):
    # consider the case where n = 7
    # instead of a[0], a[1], ..., a[n-1] I want to write a, b, c, d, e, f, g
    # s is a set, so a != b != c != d != e != f != g
    # we will sort s, so a < b < c < d < e < f < g

    # let B = [a,b,c,d] and C = [e,f,g]
    # S(B) is the smallest S(x) of cardinality 4
    # S(C) is the largest S(x) of cardinality 3

    # if a+b+c+d > e+f+g, then a+b+c > f+g because d < e
    # If a+b+c > f+g then a+b > g because c < f
    # a+b is the smallest S(B) of cardinality  2, g is the largest S(C) of cardinality 1

    # So it is sufficient to show that a+b+c+d > e+f+g. If that is true, all other
    # choices of disjoint B and C must also have property 2.

    s = sorted(s_in)
    stop = ceil(len(s)/2)
    first = s[:stop]
    second = s[-(stop-1):]
    if sum(first) <= sum(second):
        return False

    # if B and C are disjoint and S(B) != S(C), then adding a common
    #  element to each will raise each sum an equal amount, so they will continue
    #  to be !=.
    #  This allows us to relax the condition that B and C are disjoint and instead
    #  compare the sum of every subset with the sum of every other subset. If we find
    #  any match, the set in question is not a special sum subset.
    closed = set()
    for i in range(len(s)):
        for b in combinations(s, i):
            sum_b = sum(b)
            if sum_b in closed:
                return False
            closed.add(sum_b)
    return True