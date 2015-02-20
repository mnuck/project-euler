# Project Euler 3

proc maxFactor(n: int64): int64 = 
  var n = n
  var factor: int64 = 1
  while n > 1:
    factor = factor + 1
    while n mod factor == 0:
      n = n div factor
      result = factor

proc solution(): int64 = 
  maxFactor(600851475143)

echo solution()