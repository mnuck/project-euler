#!/usr/bin/env python
problem = '''
Project Euler 700
Leonhard Euler was born on 15 April 1707.

Consider the sequence 1504170715041707n mod 4503599627370517.

An element of this sequence is defined to be an Eulercoin if it is strictly smaller than all previously found Eulercoins.

For example, the first term is 1504170715041707 which is the first Eulercoin. The second term is 3008341430083414 which is greater than 1504170715041707 so is not an Eulercoin. However, the third term is 8912517754604 which is small enough to be a new Eulercoin.

The sum of the first 2 Eulercoins is therefore 1513083232796311.

Find the sum of all Eulercoins.

'''


brute_force = '''
def seq(n):
    return (1504170715041707 * n) % 4503599627370517


minCoin = 1504170715041707


def isCoin(n):
    global minCoin
    if n < minCoin:
        print("relationship", n, minCoin, n / float(minCoin))
        minCoin = n
        return True
    return False


def solution():
    result = 1504170715041707
    i = 2
    while True:
        candidate = seq(i)
        if candidate == 1504170715041707:
            return result
        if isCoin(candidate):
            result += candidate
            print(result, candidate, i)
        i += 1


def spacing():
    entries = []
    for i in range(20):
        entries.append(seq(i))
    entries.sort()
    print(entries[i+1] - entries[i])


if __name__ == "__main__":
    print(solution())
    #print(spacing())
'''


# birthday = 1504170715041707
# delta = birthday - 8912517754604
# #modulus = 4503599627370517
# minCoin = birthday


# def nextCandidate(n):
#     offset = n + (2 * birthday)
#     if offset > modulus:
#         return offset % modulus
#     remaining = modulus - offset
#     steps = remaining / spacing
#     offset += ((1+steps) * spacing)
#     return offset % modulus


# def isCoin(n):
#     global minCoin
#     global delta
#     if n < minCoin:
#         delta = minCoin - n
#         minCoin = n
#         print "discovered", minCoin, delta
#         return True
#     return False


# def discover(n):
#     while True:
#         n = nextCandidate(n)
#         if isCoin(n):
#             return n


# def generate(n):
#     global minCoin, delta
#     delta %= minCoin
#     minCoin -= delta
#     return minCoin

# if minCoin - delta > 0:
#     minCoin = minCoin - delta
#     print "generated", minCoin, delta
#     return minCoin
# delta %= minCoin
# minCoin -= delta
# print "guessed-ish", minCoin, delta
# return minCoin
# predicted = delta - minCoin
# while predicted > minCoin:
#     predicted -= minCoin
# print "predicted next delta", predicted
# return discover(n)


# def solution():
#     coin = minCoin
#     result = coin
#     while coin > 1:
#         coin = generate(coin)
#         result += coin
#     return result


def solution():
    coin = 1504170715041707
    delta = coin - 8912517754604 # second coin
    result = coin
    while coin > 1:
        delta %= coin
        coin -= delta
        result += coin
    return result


if __name__ == "__main__":
    print(solution())

