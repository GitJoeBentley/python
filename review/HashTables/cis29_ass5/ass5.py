#!/usr/bin/python3

import sys
from hash_table import Hash_table
from mystring import Mystring
from config import hash_table_size

hash_table = Hash_table()
with open("ass5words.txt") as file:         
    for line in file:
        my_s = Mystring(line[:-1].lower())
        hash_table[hash(my_s)].push(my_s)

print("Number of words in the dictionary =",len(hash_table))
print("Percent of hash table buckets used = ","{:.2f}".format(100.0 * hash_table.number_of_buckets_in_use() / hash_table_size) + '%')
print("Average non-empty bucket size = ","{:.2f}".format(hash_table.average_non_empty_bucket_size()))
print("Largest bucket size =",hash_table.largest_bucket_size())

misspelled_words = 0

with open("ihaveadream.txt") as document:
    for line in document:
        words = line.split()
        for word in words:
            new_word = Mystring(word)._remove_punctuation()
            if new_word and len(new_word) and new_word not in hash_table:
                print("Not found in the dictionary:",new_word)
                misspelled_words += 1
    print("Total mispelled words = ", misspelled_words)
