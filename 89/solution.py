#!/usr/bin/env python
#
# Project Euler 89

matchers = [('VV','X'), # compression
            ('LL','C'),
            ('DD','M'),
            ('IIII','IV'), # making fours
            ('XXXX','XL'),
            ('CCCC','CD'),
            ('VIV','IX'),  # making nines
            ('LXL','XC'),
            ('DCD','CM')]

def minimalize(s):
    global matchers
    result = s
    for matcher in matchers:
        result = result.replace(*matcher)
    return result

def solution():
    f = open("roman.txt")
    raw = f.read()
    f.close()
    shrunk = minimalize(raw)
    return len(raw) - len(shrunk)

if __name__ == "__main__":
    print solution()
