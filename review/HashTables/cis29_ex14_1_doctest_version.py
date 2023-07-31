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
    >>> animals = ("monkey","dog","cat","horse","pig","goat","hippo","dinosaur","walrus","manatee")
    >>> indexes = [hash(word) for word in animals]
    >>> indexes
    [7, 3, 1, 0, 9, 9, 9, 3, 8, 2]
    >>> hash('ABC')
    3
    >>> hash('!')
    9
    >>> "abcdefghijklmnopqrstuvwxyz".find('!')
    -1
    >>> "abcdefghijklmnopqrstuvwxyz".find('!') % NumberOfBuckets
    9

"   """

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for letter in text:
        pos = alphabet.find(letter.lower())
        sum += pos

    return sum % NumberOfBuckets


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# To run doctest: python3 -m doctest -v cis29_exercise14-1_with_doctest.py
# To display module documentations, do this:
# $ python3
# Python 3.9.16 (main, Mar  8 2023, 22:47:22)
#[GCC 11.3.0] on cygwin
#Type "help", "copyright", "credits" or "license" for more information.
# >>> import cis29_ex14_1_doctest_version
# >>> help(cis29_ex14_1_doctest_version)

