#####
### Matthew Nuckolls
### Project Euler #32
### Production Code
#####

def digits(*args):
    result = set()
    for arg in args:
        result = result.union(set([int(i) for i in str(arg)]))
    return result

def pandigital(*args):
    length = sum([len(str(arg)) for arg in args])
    if length != 9:
        return False
    d = digits(*args)
    if len(d) != length:
        return False
    else:
        return d == set(range(1,length+1))

def pandigital_product(a,b):
    return pandigital( a, b, a*b )


def small_pandigits():
    result = set()
    for a in xrange(1,10000):
        for b in xrange(1,10000):
            if pandigital_product(a,b):
                print a, b, a*b
                result.add(a*b)
    print sum(result)

small_pandigits()
