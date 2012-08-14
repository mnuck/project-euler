#!/usr/bin/env python
#
# Project Euler 99
#
# very slow

from math import log

def get_data():
    with open('base_exp.txt') as f:
        splitted = [x.split(',') for x in f.readlines()]
        data = [(int(base),int(exp)) for (base,exp) in splitted]
        result = list(enumerate(data))
    return result

def solution():
    data = get_data()
    biggest = {'value': 1, 
               'base':  1, 
               'exponent': 1, 
               'line': 0 }
    for (line, (base,exponent)) in data:
#        current = base ** exponent
        current = exponent * log(base)
        if current > biggest['value']:
            biggest = {'value': current,
                       'base': base,
                       'exponent': exponent,
                       'line': line }
    return biggest['line'] + 1
    
    
if __name__ == "__main__":
    print solution()
