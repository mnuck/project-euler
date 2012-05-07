# tests for functions in solutions.py

from solution import flushp, fourp, straightp, straight_flushp
from solution import hexify, parse_base, encode_hand, compare_hands
from solution import threep, small_pairp, big_pairp, full_housep
from solution import compare_line

def test_flush():
    assert flushp(['5H', '5C', '6S', '7S', 'KD']) == '0'
    assert flushp(['3H', '2H', 'AH', 'QH', '7H']) == 'A'
    
def test_four_of_a_kind():
    assert fourp(['5H', '5C', '6S', '7S', 'KD']) == '0'
    assert fourp(['5D', '5C', '5S', '5H', '6D']) == '5'
    assert fourp(['6D', '5C', '5S', '5H', '5D']) == '5'

def test_straight():
    assert straightp(['5H', '5C', '6S', '7S', 'KD']) == '0'
    assert straightp(['2H', '4C', '3S', '6S', '5D']) == '6'
    

def test_straight_flush():
    assert straight_flushp(['5H', '5C', '6S', '7S', 'KD']) == '0'
    assert straight_flushp(['AH', 'KH', 'QH', 'JH', 'TH']) == 'A'
    
def test_hexify():
    assert hexify('T') == 'A'
    assert hexify('2') == '2'
    assert hexify('A') == 'E'
    
def test_threep():
    assert threep(['5H', '5C', '6S', '7S', 'KD']) == '0'
    assert threep(['5H', '5C', '5S', '6S', 'KD']) == '5'
    
def test_small_pairp():
    assert small_pairp(['5H', '5C', '6S', '7S', 'KD']) == '5'
    assert small_pairp(['7H', '7C', '6S', '6S', 'KD']) == '6'

def test_big_pairp():
    assert big_pairp(['5H', '5C', '6S', '7S', 'KD']) == '0'
    assert big_pairp(['7H', '7C', '6S', '6S', 'KD']) == '7'

def test_full_housep():
    assert full_housep(['5H', '5C', '6S', '7S', 'KD']) == '0'
    assert full_housep(['7H', '7C', '6S', '6S', '6D']) == '6'

def test_parse_base():
    assert parse_base(['5H', '5C', '6S', '7S', 'KD']) == 'D7655'
    assert parse_base(['AH', 'KH', 'QH', 'JH', 'TH']) == 'EDCBA'
    
def test_encode_hand():
    assert encode_hand(['AH', 'KH', 'QH', 'JH', 'TH']) == 'E00EE000EDCBA'
    assert encode_hand(['2H', '4C', '3S', '6S', '5D']) == '0000600065432'

def test_compare_hands():
    assert compare_hands(['AH', 'KH', 'QH', 'JH', 'TH'],
                         ['2H', '4C', '3S', '6S', '5D']) == 1    
    assert compare_hands( ['2H', '4C', '3S', '6S', '5D'],
                          ['AH', 'KH', 'QH', 'JH', 'TH'] ) == -1

    
def test_compare_line():
    assert compare_line('AH KH QH JH TH 2H 4C 3S 6S 5D') == 1
    assert compare_line('2H 4C 3S 6S 5D AH KH QH JH TH') == -1
