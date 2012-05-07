###
### Project Euler 54
###
### Given a thousand poker hands, determine how many times player 1 wins

# A hand can be encoded into a hex integer so a simple < can find the winner

rank_table = { '0': 0, '2': 2, '3': 3, '4': 4, 
               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }

def hexify(rank):
    """Returns a single uppercase hexadecimal digit"""
    return hex(rank_table[rank])[-1].upper()


def parse_base(hand):
    """Base value of a hand, not counting anything but card values"""
    in_order = sorted(hand, key=lambda x: rank_table[x[0]], reverse=True)
    return ''.join([hexify(x[0]) for x in in_order])


def _make_rank_histogram(hand):
    """Generate a histogram of how many cards of each rank are in a hand"""
    hist = { k:0 for (k,v) in rank_table.iteritems() } 
    for rank in [x[0] for x in hand]:
        hist[rank] += 1
    return hist


def _cardinalities(hand):
    hist = _make_rank_histogram(hand)
    items = hist.items()
    result = {'four': '0', 'three': '0', 'small': '0', 'big': '0', 'full': '0'}
    if 4 in hist.values():
        result['four'] = [x[0] for x in items if x[1]==4][0]
    if 3 in hist.values():
        result['three'] = [x[0] for x in items if x[1]==3][0]
    pairs = [x[0] for x in hist.items() if x[1] == 2]
    if len(pairs) == 1:
        result['small'] = pairs[0]
    if len(pairs) == 2:
        result['big']   = max(pairs, key=lambda x: rank_table[x])
        result['small'] = min(pairs, key=lambda x: rank_table[x])
    if '0' not in (result['three'], result['small']):
        result['full'] = result['three']
    return result


def _straight_flush(hand, parsed_hand):
    result = {'straight': '0', 'flush': '0', 'straight_flush': '0'}
    hand.sort(key=lambda x: rank_table[x[0]], reverse=True)
    if all([x=='0' for x in parsed_hand.values()]):
        if rank_table[hand[0][0]] - rank_table[hand[-1][0]] == 4:
            result['straight'] = hand[0][0]
    if all([x[1] == hand[0][1] for x in hand]):
        result['flush'] = hand[0][0]
    if '0' not in (result['flush'], result['straight']):
        result['straight_flush'] = result['straight']
    return result


def encode_hand(hand):
    parsed_hand = _cardinalities(hand)
    parsed_hand.update( _straight_flush(hand, parsed_hand) )
    result = ''
    for key in ['straight_flush', 'four', 'full', 'flush',
                'straight', 'three', 'big', 'small']:
        result += hexify(parsed_hand[key])
    result += parse_base(hand)
    print hand, result
    return result


def compare_hands(a, b):
    a_value, b_value = [int(encode_hand(x), 16) for x in [a, b]]
    if a_value > b_value:
        return 1
    elif a_value < b_value:
        return -1
    else:
        return 0

    
def compare_line(line):
    cards = line.split(' ')
    return compare_hands( cards[:5], cards[5:] )


def main():
    with open('poker.txt', 'r') as f:
        lines = f.readlines()
    
    scoreboard = {1: 0, -1: 0, 0: 0}
    for line in lines:
        scoreboard[ compare_line(line[:-2]) ] += 1
    print scoreboard[1]
    
    
if __name__ == '__main__':
    main()

    
def small_pairp(hand):
    return _cardinalities(hand)['small']

def big_pairp(hand):
    return _cardinalities(hand)['big']

def threep(hand):
    return _cardinalities(hand)['three']

def fourp(hand):
    return _cardinalities(hand)['four']

def full_housep(hand):
    return _cardinalities(hand)['full']

def straightp(hand):
    return _straight_flush(hand)['straight']

def flushp(hand):
    return _straight_flush(hand)['flush']

def straight_flushp(hand):
    return _straight_flush(hand)['straight_flush']


