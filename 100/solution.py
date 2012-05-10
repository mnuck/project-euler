from math import sqrt

prev_i, i = 5, 29
multiplier = i / float(prev_i)
total = 0
while total < 10 ** 12:
    m = 2*i*i - 1
    n = int(sqrt(m))
    total, blue = [(1+x)/2 for x in (n, i)]
    prev_i, i = i, int(i * multiplier)
    if i % 2 == 0: # ensure oddness
        i += 1

    multiplier = i / float(prev_i)

print blue
