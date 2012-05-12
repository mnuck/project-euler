from math import sqrt

def isPentagonal(n):
    x = (sqrt(6*n + 0.25) + 0.5)/3
    return x == int(x)

def genHex(n):
    return n * (2*n - 1)

solution = (genHex(n) 
            for n in xrange(144,50000)
            if isPentagonal(genHex(n))).next()

print solution
