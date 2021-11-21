#!/usr/bin/env python

def set_string(s):
    result = ""
    for item in sorted(s):
        result += str(item)  # string concatenate
    return result

def solution():
    return set_string([1,2,3,4,5])

if __name__ == "__main__":
    print(solution())

