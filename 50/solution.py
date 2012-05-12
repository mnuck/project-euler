# Project Euler 50
#
# The prime 41, can be written as the sum of six consecutive primes: 
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes 
# that adds to a prime below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand 
# that adds to a prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of 
# the most consecutive primes?

def cached_primes():
    with open("primes1000000.txt", 'r') as f:
        result = [int(x) for x in f.readlines()]
    return result

primes = cached_primes()

def consec_sum(n):
	i = primes.index(n)/2 + 1
	maxlen = 0
	while i > 0:
		j = i
		a = primes[j]
		while a < n:
			j -= 1
			a += primes[j]
		if a == n:
			if i - j > maxlen:
				maxlen = i - j
		i -= 1
	return maxlen + 1


maxlen = 0
for prime in primes:
	l = consec_sum(prime)
	if l > maxlen:
		maxlen = l
		print prime, l
