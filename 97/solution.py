a = 28433
for i in xrange(7830457):
    a *= 2
    a %= 10000000000
a += 1
print a
