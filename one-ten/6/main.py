#!/usr/bin/env python

nums = range(1,101)
square_of_sum = sum(nums) * sum(nums)
print square_of_sum

squares = map(lambda x: x*x, nums)
sum_of_squares = sum(squares)
print sum_of_squares

difference = square_of_sum - sum_of_squares
print difference