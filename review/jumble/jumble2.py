#! /usr/local/bin/python3

import sys
from math import prod

# primes is a tuple of the first 26 prime numbers
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)

# words is a list of tuples to hold each word and its "encoded value"
words = []

def encode(word: str):
    """ Returns product of primes associated with each letter in word
        Return None is word contains non alpha characters
    """
    try:
        primes_in_word = [primes[ord(letter) - ord ('A')] for letter in word if letter < 'A' or letter > 'Z']
        return prod(primes_in_word)
    except IndexError as e:
        print(e)
        return None
"""
    product = 1
    for letter in word:
        if letter < 'A' or letter > 'Z':
            return None
        product = product * primes[ord(letter) - ord ('A')]
    return product
"""

# Read words from "words" file.  Encode each word and list of tuples
words = [(word, encode(word)) for word in [word.rstrip().upper() for word in open("words")]]

# Get jumbled word from commandline and encode
#coded_word = encode(sys.argv[1].upper())
coded_word = encode("PPYHA")

print([entry[0] for entry in words if coded_word == entry[1]])
