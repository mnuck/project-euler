#####
### Project Euler #42
### Production Code
#####

_triangle_numbers = {1:1, 3:2, 6:3}

def _biggest_triangle():
    global _triangle_numbers
    return max([k for k in _triangle_numbers])

def _grow_triangles():
    global _triangle_numbers
    next_n = 1 + max([_triangle_numbers[k] for k in _triangle_numbers])
    _triangle_numbers[int(0.5 * next_n * (next_n+1))] = next_n
    
def trianglep(x):
    global _triangle_numbers
    while x > _biggest_triangle():
        _grow_triangles()
    if x in _triangle_numbers:
        return True
    return False

_character_numbers = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
                       'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j':10,
                       'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
                       'p':16, 'q':17, 'r':18, 's':19, 't':20,
                       'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26 }

def _char2num(c):
    global _character_numbers
    return _character_numbers[c]

def word2num(word):
    if word:
        return sum([_char2num(c) for c in word.lower()])
    else:
        return 0

def triangle_wordp(word):
    return trianglep(word2num(word))

wordlist = list()
def load_wordlist():
    global wordlist
    f = open("words.txt", 'r')
    wordlist = [ x[1:-1] for x in f.read().split(',') ]
    f.close()
    
def get_word(x):
    global wordlist
    return wordlist[x]

def solution():
    global wordlist
    load_wordlist()
    triangle_words = [x for x in wordlist if triangle_wordp(x)]
    return len(triangle_words)

print solution()
