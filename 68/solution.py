#!/usr/bin/env python
#
# Project Euler 68

atoms = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
from itertools import permutations
def childrens(current, total):
    global atoms
    unused = atoms - set(current)
    if len(unused) == 1:
        a, b, c = current[-1], current[1], unused.pop()
        if sum([int(a), int(b), int(c)]) == total:            
            return [current + [c, a, b]]
        return []
    result = list()
    for (a, b) in permutations(unused, 2):
        if sum([int(a), int(b), int(current[-1])]) == total:            
            result.append(current + [a, current[-1], b])
    return result


def starters(total):
    global atoms
    result = list()
    for (a, b, c) in permutations(atoms, 3):
        if a == '10':
            if sum([int(x) for x in (a, b, c)]) == total:
                result.append([a, b, c])
    return result
            

def partial(current, total):
    for kid in childrens(current, total):
        if len(kid) == 15: # MAGIC NUMBER
            return kid
        result = partial(kid, total)
        if result:
            return result
    return False


def score(s):
    minval = min([int(x) for x in s[::3]])
    index = s.index(str(minval))
    return int("".join(s[index:] + s[:index]))

    
def stupid_thing(total):
    result = set()
    for starter in starters(total):
        attempt = partial(starter, total)
        if attempt:
            result.add(score(attempt))
#    print total, result
    return max(result) if result else False

def solution():
    global atoms
    min_possible = min([int(x) for x in atoms])
    min_possible = 3 * min_possible + 3
    
    max_possible = max([int(x) for x in atoms])
    max_possible = 3 * max_possible - 3
    
    result = list()
    for i in xrange(min_possible, max_possible+1):
        result.append(stupid_thing(i))
    return max(result)


if __name__ == "__main__":
    print solution()
