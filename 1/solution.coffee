#!/usr/bin/env coffee

fives    = (n) -> n % 5 is 0
threes   = (n) -> n % 3 is 0
members  = (n for n in [1...1000] when fives(n) or threes(n))
solution = members.reduce (x, y) -> x + y
console.log solution
