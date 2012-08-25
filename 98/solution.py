#!/usr/bin/env python
#
# Project Euler 98

from collections import Counter  # anagram finder

'''we only need squares up to 9 digits'''
squares = set()
base = 1
square = base * base
while square < 999999999:
    squares.add(square)
    base += 1
    square = base * base


def get_words():
    with open('words.txt') as f:
        data = f.readline()
    return [x[1:-1] for x in data.split(',')]


def get_anagrams():
    #return [['care', 'race']]
    collider = dict()
    for word in get_words():
        key = tuple(dict(Counter(word)).items())
        if key not in collider:
            collider[key] = list()
        collider[key].append(word)
    return [x for x in collider.values() if len(x) > 1]


def remap(n, anagram):
    '''treats the anagram pair as a recipie for reordering digits of n'''
    n = str(n)
    result = list()
    for digit in anagram[0]:
        position = anagram[1].index(digit)
        result.append(n[position])
    return int(''.join(result))


def no_repeats(n):
    return len(str(n)) == len(set(str(n)))
    

def find_best(anagram):
    result = set([False])
    candidates = set([x for x in squares if len(str(x)) == len(anagram[0])])
    for candidate in candidates:
        if not no_repeats(candidate):
            continue
        possible = remap(candidate, anagram)
        if possible != candidate and possible in candidates:
            result.add(candidate)
    return max(result)


def solution():
    return max(find_best(anagram) for anagram in get_anagrams())


if __name__ == "__main__":
    print solution()
