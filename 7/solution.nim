# Project Euler 7

from primes import isPrime

proc solution(): int =
  var n = 1
  var i = 0
  while i < 10_001:
    n = n + 1
    if isPrime(n):
      i = i + 1
  result = n

echo solution()
