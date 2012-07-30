#####
### Matthew Nuckolls
### Project Euler #43
### Production Code
#####

def pandigital(string):
    if len(string) != 10:
        return False
    if len(set([c for c in string])) != 10:
        return False
    return True

def rule1(string):
    return int(string[3]) % 2 == 0

def rule2(string):
    return int(string[2:5]) % 3 == 0

def rule3(string):
    return int(string[3:6]) % 5 == 0

def rule4(string):
    return int(string[4:7]) % 7 == 0

def rule5(string):
    return int(string[5:8]) % 11 == 0

def rule6(string):
    return int(string[6:9]) % 13 == 0

def rule7(string):
    return int(string[7:10]) % 17 == 0

def all_rules(string):
    for rule in [pandigital, rule1, rule2, rule3, rule4, rule5, rule6, rule7]:
        if not rule(string):
            return False
    return True

def solution():
    i = 1023456789
    sum = 0
    while( i < 9876543211 ):
        if all_rules(str(i)):
            print i
            sum += i
        i += 1
    print sum

solution()
