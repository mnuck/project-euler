

def cached_4digit_prime_strings():
    with open("primes1000000.txt", 'r') as f:
        result = [(tuple(sorted(list(x.strip('\n')))), int(x)) 
                  for x in f.readlines() 
                  if len(x) == 5]
    return result


prime_digits = cached_4digit_prime_strings()

perm_sets = dict()

for (digits, number) in prime_digits:
    if digits not in perm_sets:
        perm_sets[digits] = list()
    perm_sets[digits].append(number)

for key in perm_sets:
    perm_sets[key].sort()

filtered_perm_sets = [v for (k,v) in perm_sets.items() if len(v) >= 3]

def isArithmeticSequence(x):
    return x[2] - x[1] == x[1] - x[0]

from itertools import combinations

for group in filtered_perm_sets:
    for triple in combinations(group,3):
        if isArithmeticSequence(triple):
            print triple, ''.join([str(x) for x in triple])

