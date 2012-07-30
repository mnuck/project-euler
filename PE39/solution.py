#####
### Matthew Nuckolls
### Project Euler #39
### Production Code
#####

def is_right_triangle(a, b, c):
    return a*a + b*b == c*c

def valid_triangles(p):
    result = list()
    for a in xrange(1,p):
        for b in xrange(1,a):
            c = p - (a + b)
            if is_right_triangle(a, b, c):
                result.append( (a, b, c) )
    return result

def solution():
    print max(xrange(1,1001), key=lambda x: len(valid_triangles(x)))

solution()
