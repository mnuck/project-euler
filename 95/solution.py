#!/usr/bin/env python
#
# Project Euler 95

"""
For each number n, there exist three possibilities:
1. a chain starting from n will return to n (amicable)
2. a chain starting from n will end at zero (breaker)
3. a chain starting from n will return to a number m that is part of
   the chain starting at n (tail)

Well that was a disappointingly low number. It's the smallest
of the chain of length 28.
"""

amicable = set()
breaker = set([0])
tail = set()
chains = dict()


def divisors(n):
    result = list()
    for trial in xrange(1, (n / 2) + 1):
        if n % trial == 0:
            result.append(trial)
    return result


def next(n):
    return sum(divisors(n))


def categorize(n):
    '''decide if n is amicable, breaker, or tail'''
    chain = set()
    start = n
    while n not in chain:
        chain.add(n)
        n = next(n)
        if n in breaker:
            breaker.update(chain)
            return
        if n > 1000000:
            breaker.update(chain)
            return
        if n in amicable:
            if n == start:
                amicable.update(chain)
            else:
                tail.add(start)
            return
    if n == start:
        amicable.update(chain)
    else:
        tail.add(start)


def chain(n):
    result = list()
    while n not in result:
        result.append(n)
        n = next(n)
    return result


def chain_length(n):
    if n in chains:
        return chains[n]
    c = chain(n)
    for a in c:
        chains[a] = len(c)
    return chains[n]


def solution():
    for i in xrange(2, 20001, 2):
        categorize(i)
        if i % 2000 == 0:
            print i
    print amicable
    longest = 1
    for a in amicable:
        if chain_length(a) > longest:
            longest = chain_length(a)
            member = a
            print a, chain_length(a)
    longest = chain(member)
    return min(longest)


if __name__ == "__main__":
    print solution()
