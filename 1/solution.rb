#!/usr/bin/env ruby

def threes(n)
    return n % 3 == 0
end

def fives(n)
    return n % 5 == 0
end

members = (1..1000).select do |elem|
    threes(elem) || fives(elem)
end

solution = members.reduce(:+)
puts solution