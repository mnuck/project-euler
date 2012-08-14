#!/usr/bin/env python
#
# Project Euler 99
#
# very slow

def get_data():
    with open('base_exp.txt') as f:
        splitted = [x.split(',') for x in f.readlines()]
        data = [(int(base),int(exp)) for (base,exp) in splitted]
        result = list(enumerate(data))
    return result

def solution():
    data = get_data()
    biggest = {'value': 1**1, 
               'base':  1, 
               'exponent': 1, 
               'line': 0 }
    for (line, (base,exponent)) in data:
        current = base ** exponent
        if current > biggest['value']:
            print "new winnar:", line, base, exponent
            biggest = {'value': current,
                       'base': base,
                       'exponent': exponent,
                       'line': line }
        else:
            print "loser!", line
    return biggest['line'] + 1
    
    
if __name__ == "__main__":
    print solution()
