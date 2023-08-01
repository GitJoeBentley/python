#! /usr/bin/python3

"""
This python module is a solution for the CIS29 example 14-2 located at 
http://voyager.deanza.edu/~bentley/cis29/examples/ex14-2.cpp
"""

__author__ = "Joe Bentley, joe.deanza@gmail.com"

class Dictionary:
    def __init__(self, filename: str):
        self._dictionary = (open(filename).read().split('\n'))
        

def hash(text: str) -> int:
    """
    :return: a hashed value for text.  This is used as an index in a "hash table"
    :param text: word to be hashed
    """

    primes[26] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                  79, 83, 89, 97, 101};
    product = 1;
    for letter in text:
        product *= primes[ord(tolower(letter))  - ord('a')]
    return product % number_of_buckets

if __name__ == '__main__':
    dictionary = Dictionary('words')
                            
