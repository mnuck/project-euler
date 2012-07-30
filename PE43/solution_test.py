#####
### Matthew Nuckolls
### Project Euler #43
### Test Code
#####

from solution import pandigital
from solution import rule1, rule2, rule3, rule4, rule5, rule6, rule7
from solution import all_rules

def pandigital_test():
    assert not pandigital("")
    assert not pandigital("123456789")
    assert pandigital("1234567890")
    assert not pandigital("1111111111")
    assert pandigital("9876540123")

def test_rules():
    for rule in [rule1, rule2, rule3, rule4, rule5, rule6, rule7]:
        assert rule("1406357289")

def test_all_rules():
    assert all_rules("1406357289")
    
