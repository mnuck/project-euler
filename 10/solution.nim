# Project Euler 10
# Sum of primes < 2_000_000

type bools = array[2_000_000, bool]

proc solution(): int64 =
  var a: bools
  a[0] = true
  a[1] = true
  var i = 2
  while i < 1_000_000:
    result += i
    for j in countup(2*i, 1_999_999, i):
      a[j] = true
    i += 1
    while a[i]:
      i += 1
  while i < 2_000_000:
    if a[i] == false:
      result += i
    i += 1

echo solution()