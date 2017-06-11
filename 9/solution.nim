# Project Euler 9

# a, b, c are natural numbers
# a < b < c
# a^2 + b^2 = c^2
# a + b + c = 1000
# return a * b * c

proc solution(): int =
  for b in 1..1000:
    for a in 1..b:
      let c: int = 1000 - (a + b)
      if a * a + b * b == c * c:
        return a * b * c
  return -1

echo solution()