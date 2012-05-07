#!/usr/bin/env python

fib_prev1 = 1
fib_prev2 = 2
total = 2

fib_current = fib_prev1 + fib_prev2
while( fib_current < 4000000 ):
  if( fib_current % 2 == 0 ):
    total += fib_current
  fib_prev1 = fib_prev2
  fib_prev2 = fib_current
  fib_current = fib_prev1 + fib_prev2

print total