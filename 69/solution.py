#
# Project Euler 69
# 

def cached_primes():
    with open("primes100000.txt", 'r') as f:
        result = [int(x) for x in f.readlines()]
    return result

primes = cached_primes()

def prime_factors(n):
    result = set()
    while n > 1:
        for prime in primes:
            if n % prime == 0:
                result.add(prime)
                n = n / prime
                break        
    return result

factormap = { x: prime_factors(x) for x in xrange(2,1000001) }

print "here!"

def totient(n):
    factors = factormap[n]
    result = 1
    for i in xrange(2,n):
        if not factors.intersection(factormap[i]):
            result += 1
    return result

maxratio = 0
for i in xrange(2,1000001):
    ratio = float(i)/totient(i)
    if ratio > maxratio:
        maxratio = ratio
        print i, ratio
        
