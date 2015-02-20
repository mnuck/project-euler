# Project Euler 2

iterator fibs(upTo: int): int =
  yield 0
  var previous = 0
  var current = 1
  var next = previous + current
  while current <= upTo:
    yield current
    previous = current
    current = next
    next = previous + current

proc solution(): int = 
  for i in fibs(upTo = 4_000_000):
    if (i mod 2 == 0):
      result = result + i

echo solution()