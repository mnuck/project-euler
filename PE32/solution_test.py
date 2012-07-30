#####
### Matthew Nuckolls
### Project Euler #32
### Test Code
#####

from solution import digits, pandigital, pandigital_product

def digits_test():
    assert digits(1234) == set([1, 2, 3, 4])
    assert digits(12) == set([1, 2])
    assert digits(12,34,51) == set([1,2,3,4,5])
    
def pandigital_test():
    assert pandigital( 1234, 567 )
    assert not pandigital( 234 )
    
def pandigital_product_test():
    assert pandigital_product(39, 186)
    
