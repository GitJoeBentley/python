#!/usr/bin/python3

import sys
from hash_table import Hash_table
from mystring import Mystring

hash_table = Hash_table()
with open("ass5words.txt") as file:         
    for line in file:
        hash_table.insert(line[:-1].lower())

print("Number of words in the dictionary =",hash_table._number_in_table)
print("Percent of hash table buckets used = ","{:.2f}".format(100.0 * hash_table._in_use / hash_table._size) + '%')
print("Average non-empty bucket size = ","{:.2f}".format(hash_table.average_non_empty_bucket_size()))
print("Largest bucket size =",hash_table.largest_bucket_size())

misspelled_words = 0

with open("ihaveadream.txt") as document:
    for line in document:
        words = line.split()
        for word in words:
            new_word = Mystring(word.lower())._remove_punctuation()
            index = hash(new_word) % hash_table._size
            if len(new_word) and new_word not in hash_table:
                print("Not found in the dictionary:",new_word)
                misspelled_words += 1
    print("Total mispelled words = ", misspelled_words)
