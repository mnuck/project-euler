# Project Euler 4

proc isPalindrome(n: int): bool =
  let s = $n
  for i in 0..(s.len div 2):
    if s[i] != s[s.len - (i + 1)]:
       return false
  return true

proc solution(): int = 
  for i in 100..999:
    for j in 100..999:
      let product = i * j
      if isPalindrome(product):
        if product > result:
          result = product

echo solution()