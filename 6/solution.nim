# Project Euler 6

proc squareOfSum(n: int): int = 
  ## sum(1..n) == n(n+1)/2
  result = n * (n + 1) div 2
  result = result * result

proc sumOfSquares(n: int): int = 
  ## sum(1^2..n^2) = n(n+1)(2n+1)/6
  result = n * (n + 1) * (2*n + 1) div 6

proc solution(): int =
  squareOfSum(100) - sumOfSquares(100)

echo solution()