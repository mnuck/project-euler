#####
### Project Euler #42
### Test Code
#####

# Read words.txt into a list of strings
# Check if a word is a triangle word
# Convert a word into a number
# Check if a number is a triangle number
# Count the number of triangle numbers in a list

from solution import trianglep, word2num, triangle_wordp
from solution import load_wordlist, get_word, solution

def trianglep_test():
    assert trianglep(1) == True
    assert trianglep(2) == False
    assert trianglep(3) == True
    assert trianglep(45) == True
    assert trianglep(36) == True

def word2num_bare_input_test():
    assert word2num('') == 0
    
def word2num_string_test():
    assert word2num('sky') == 55
    assert word2num('a') == 1
    assert word2num('SKY') == 55
    
def triangle_wordp_test():
    assert triangle_wordp('sky') == True
    assert triangle_wordp('SKY') == True
    assert triangle_wordp('b') == False
    
def load_wordlist_test():
    load_wordlist()
    assert get_word(0) == 'A'
    assert get_word(1) == 'ABILITY'

def main_test():
    solution()
