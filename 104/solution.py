#!/usr/bin/env python

def fibs(modulo=0):
	previous = 0
	current = 1
	while True:
                if modulo > 0:
                        current %= modulo
		yield current
		temp = current
		current += previous
		previous = temp

def pandigital_string(s):
	return "123456789" == "".join(sorted(list(s)))

def pandigital_bottom(s):
	return pandigital_string(s[-9:])

def pandigital_top(s):
	return pandigital_string(s[:9])

bottoms = set()

def solution():
	i = 0
	for fib in fibs(1000000000):
		i += 1
		s = str(fib)
		bottom = pandigital_bottom(s)
		if bottom:
			bottoms.add(i)
		if i > 1000000:
			break

	i = 0
	for fib in fibs():
		i += 1
		if i in bottoms:
			if pandigital_top(str(fib)):
				return i

if __name__ == "__main__":
	print solution()

