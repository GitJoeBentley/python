#! /usr/bin/python3

"""
This python module is a solution for the CIS29 example 14-1 located at 
http://voyager.deanza.edu/~bentley/cis29/examples/ex14-1.cpp
"""

__author__ = "Joe Bentley, joe.deanza@gmail.com"

NumberOfBuckets = 10

def hash(text: str) -> int:
    """
    :return: the sum of index values for each letter of a word
    :param text: word to be hashed
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for letter in text:
        pos = alphabet.find(letter.lower())
        sum += pos

    return sum % NumberOfBuckets


if __name__ == '__main__':
    animals = ("monkey","dog","cat","horse","pig","goat","hippo","dinosaur","walrus","manatee")
    hashed_animals = [None for i in range(NumberOfBuckets)]
    for word in animals:
        index = hash(word)
        if hashed_animals[index] is None:
            hashed_animals[index] = word
        else:
            print('Can\'t store', word + '.  Bucket', index, 'is already taken')

    for i in range(NumberOfBuckets):
        print(i,(hashed_animals[i] if hashed_animals[i] else ''))
