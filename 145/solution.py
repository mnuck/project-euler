#!/usr/bin/env pypy

def digits(n):
    while n > 0:
        yield n % 10
        n /= 10

def trailing_zero(n):
    return n % 10 == 0

def reverse_digits(n):
    result = 0
    for digit in digits(n):
        result *= 10
        result += digit
    return result

def odd(n):
    return n % 2 == 1

def all_digits_odd(n):
    return all(odd(digit) for digit in digits(n))

def reversible(n):
    return not trailing_zero(n) and all_digits_odd(n + reverse_digits(n))

def solution(n):
    result = 0
    for i in xrange(1, n):
      if reversible(i):
        result += 1
    return result

if __name__ == "__main__":
    print solution(1000000000)
