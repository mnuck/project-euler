# Project Euler 5

proc greatestCommonDivisor(a, b: int): int =
  result = a
  var b = b
  var temp: int
  while b != 0:
    temp = b
    b = result mod b
    result = temp

proc leastCommonMultiple(a,b: int): int = 
  a div greatestCommonDivisor(a, b) * b

proc solution(): int =
  result = 1
  for i in 2..20:
    result = leastCommonMultiple(result, i)

echo solution()