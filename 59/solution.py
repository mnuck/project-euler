#!/usr/bin/env python
# Project Euler 59
#

words = ["and", "the", "was"]

def crypt(a, b):
    return [x^y for (x,y) in zip(a,b)]

def stringify(a):
    return ''.join([chr(x) for x in a])

with open("cipher1.txt", 'r') as f:
    cyphertext = [int(x) for x in f.read().split(',')]
    
numbers = [ord(x) for x in  "abcdefghijklmnopqrstuvwxyz"]
for i in numbers:
    for j in numbers:
        for k in numbers:
            keytext = [i, j, k] * (len(cyphertext)/3 + 1)
            decrypt = crypt(keytext, cyphertext)
            plaintext = stringify(decrypt)
            if all(x in plaintext for x in words):
                print plaintext
                print sum(decrypt)
