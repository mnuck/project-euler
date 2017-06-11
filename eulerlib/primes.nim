# primes.nim
# functions useful for handling primes in Project Euler problems

proc powMod *(b, e, m: int): int =
  assert e >= 0
  var e = e
  var b = b
  result = 1
  while e > 0:
    if e mod 2 == 1:
      result = (result * b) mod m
    e = e div 2
    b = (b * b) mod m

proc tryComposite(a, d, n, s: int): bool =
  var x = powmod(a, d, n)
  if x in [1, n - 1]:
    return false
  for i in 1..(s-1):
    x = powmod(x, 2, n)
    if x == n - 1:
      return false
  return true

proc isPrime *(n: int): bool =
  if n in [2, 3]:
    return true
  var d = n - 1
  var s = 0
  while d mod 2 == 0:
    d = d div 2
    s = s + 1
  # magic numbers from http://miller-rabin.appspot.com/
  for a in [2, 3, 325, 9375, 28178, 450775, 9780504, 1795265022]:
    if a > (n - 2):
      return true
    if tryComposite(a, d, n, s):
      return false
  return true
