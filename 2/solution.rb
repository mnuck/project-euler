#!/usr/bin/env ruby
# Project Euler #2

previous_fib = 1
current_fib = 2
solution = 2

next_fib = previous_fib + current_fib
while next_fib < 4000000 do
    if next_fib % 2 == 0 then
        solution += next_fib
    end
    previous_fib = current_fib
    current_fib = next_fib
    next_fib = previous_fib + current_fib
end

puts solution