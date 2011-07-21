#!/usr/bin/env python

def numToWordLetterCount(n):
  ones = { 0  : 0, # "",
           1  : 3, # "one",
           2  : 3, # "two",
           3  : 5, # "three",
           4  : 4, # "four",
           5  : 4, # "five",
           6  : 3, # "six",
           7  : 5, # "seven",
           8  : 5, # "eight",
           9  : 4, # "nine",
           10 : 3, # "ten",
           11 : 6, # "eleven",
           12 : 6, # "twelve",
           13 : 8, # "thirteen",
           14 : 8, # "fourteen",
           15 : 7, # "fifteen",
           16 : 7, # "sixteen",
           17 : 9, # "seventeen",
           18 : 8, # "eighteen",
           19 : 8 }# "nineteen" }

  tens = { 20 : 6, # "twenty",
           30 : 6, # "thirty",
           40 : 5, # "forty",
           50 : 5, # "fifty",
           60 : 5, # "sixty",
           70 : 7, # "seventy",
           80 : 6, # "eighty",
           90 : 6 }# "ninety" }

  if( n < 20 ):
    return ones[n]
  elif( n < 100 ):
    return tens[ n / 10 * 10] + ones[ n % 10 ]
  elif( n < 1000 ):
    if( n % 100 == 0 ):
      return numToWordLetterCount( n / 100 ) + 7
    else:
      return numToWordLetterCount( n / 100 ) + \
             numToWordLetterCount( n % 100 ) + 10
  elif( n == 1000 ):
    return 11 # "one thousand"

print sum( [numToWordLetterCount(x) for x in range(1,1001)] )
