#! /usr/bin/python3

import sys

# primes is a tuple of the first 26 prime numbers
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)

# words is a dictionary to hold each word and its "encoded value"
words = {}

def encode(word: str):
    """ Returns product of primes associated with each letter in word
        Return None is word contains non alpha characters
    """
    product = 1
    for letter in word:
        if letter < 'A' or letter > 'Z':
            return None
        product = product * primes[ord(letter) - ord ('A')]
    return product

# Read words from "words" file.  Encode each word and insert into dictionary
file = open("words")
for line in file:
    # remove newline from each line and convert to uppercase
    line = line.rstrip().upper()  
    code = encode(line)
    if code:
        words[line] = code

# Get jumbled word from commandline
#jumbled_word = sys.argv[1].upper()
jumbled_word = 'YPHAP'

coded_word = encode(jumbled_word)

# Search through all words in the dictionary to find any with same encoded value as the jumbled word
for key, value in words.items():
    if value == coded_word:
        print(key)