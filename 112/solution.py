#!/usr/bin/env python
#
# Project Euler 112

def bouncy(n):
	if n < 100:
		return False
	increasing = False
	decreasing = False
	digit = n % 10
	while n > 9:
		n = n / 10
		next_digit = n % 10
		if next_digit > digit:
			increasing = True
		if next_digit < digit:
			decreasing = True
		digit = next_digit

	return (increasing and decreasing)


def solution():
	i = 0
	bouncy_count = 0
	unbouncy_count = 0
	stop_ratio = 0.99
	ratio = 0.1
	while ratio < stop_ratio:
		i += 1
		if bouncy(i):
			bouncy_count += 1
		else:
			unbouncy_count += 1
		ratio = float(bouncy_count) / (bouncy_count + unbouncy_count)

	return i


if __name__ == "__main__":
	print solution()