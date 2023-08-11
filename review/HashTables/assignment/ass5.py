#!/usr/bin/python3

from hash_table import Hash_table
from hash_table import DuplicateError
from mystring import Mystring

hash_table = Hash_table()
with open("ass5words.txt") as file:         
    for line in file:
        my_s = Mystring(line[:-1].lower())
        try:
            hash_table.add(my_s)
        except DuplicateError as e:
            print(e)

misspelled_words = 0

with open("ihaveadream.txt") as document:
    for line in document:
        words = line.split()
        for word in words:
            new_word = Mystring(word)._remove_punctuation()
            if new_word and new_word not in hash_table:
                print("Not found in the dictionary:",new_word)
                misspelled_words += 1
    print("Total mispelled words = ", misspelled_words)
