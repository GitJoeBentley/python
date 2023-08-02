#! /usr/bin/python3

"""
This python module is a solution for the CIS29 example 14-2 located at 
http://voyager.deanza.edu/~bentley/cis29/examples/ex14-2.cpp
"""

__author__ = "Joe Bentley, joe.deanza@gmail.com"

number_of_buckets = 100000

class Dictionary:
    def __init__(self, filename: str):
        self._dictionary = [None for i in range(number_of_buckets)]
        temp = (open(filename).read().split('\n'))
        self._number_of_words = len(temp)
        self._number_of_words_not_stored = 0
        self._number_of_buckets_used = 0
        for word in temp:
            index = hash(word)
            if index and not self._dictionary[index]:
                self._dictionary[index] = word
                self._number_of_buckets_used += 1
            else:
                self._number_of_words_not_stored += 1
        print("number of buckets used = ", self._number_of_buckets_used)
        print("number of words not stored =" , self._number_of_words_not_stored)
        print("number of words = ", self._number_of_words),

    def find_scambled_word(self, scramble_word: str) -> str:
        index = hash(scramble_word)
        word = self._dictionary[index]
        return word
        

def hash(text: str) -> int:
    """
    :return: a hashed value for text.  This is used as an index in a "hash table"
    :param text: word to be hashed
    """

    primes =(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                  79, 83, 89, 97, 101)
    product = 1;
    for letter in text:
        index = ord(letter.lower())  - ord('a')
        if index < 0 or index >= len(primes):
            return None
        product *= primes[index]
    return product % number_of_buckets


if __name__ == '__main__':
    dictionary = Dictionary('words')
    while (True):
        scrambled_word = input('Enter a scrambled word (\"quit\" to exit) => ')
        if scrambled_word == 'quit':
            exit(0)
        else:
            print('unscramble =',dictionary.find_scambled_word(scrambled_word))                              
                            
