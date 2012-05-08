#
# Project Euler 33
#
# Find fractions where stupid-cancelling actually works

def left(x):
    return x / 10

def right(x):
    return x % 10

solution = 1
for denominator in xrange(11,100):
    for numerator in xrange(11,denominator):
        if right(denominator) == 0 or right(numerator) == 0:
            continue
        if left(numerator) == right(denominator):
            true = float(numerator)/denominator
            approx = float(right(numerator))/left(denominator)
            if true == approx:
                print numerator, "/", denominator, true, approx
                solution *= true
        elif right(numerator) == left(denominator):
            true = float(numerator)/denominator            
            approx = float(left(numerator))/right(denominator)
            if true == approx:
                print numerator, "/", denominator, true, approx
                solution *= true

print 1/solution
