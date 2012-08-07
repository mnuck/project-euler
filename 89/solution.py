#!/usr/bin/env python
#
# Project Euler 89

matchers = [('VV','X'),    # compression
            ('LL','C'),
            ('DD','M'),
            ('IIII','IV'), # making fours
            ('XXXX','XL'),
            ('CCCC','CD'),
            ('VIV','IX'),  # making nines
            ('LXL','XC'),
            ('DCD','CM')]

def minimalize(s):
    for matcher in matchers:
        s = s.replace(*matcher)
    return s

def solution():
    with open("roman.txt") as f:
        raw = f.read()
    return len(raw) - len(minimalize(raw))

if __name__ == "__main__":
    print solution()
