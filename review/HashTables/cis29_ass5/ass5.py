#!/usr/bin/python3

import sys
from hash_table import Hash_table
from mystring import Mystring

hash_table = Hash_table()
with open("ass5words.txt") as file:         
    for line in file:
        hash_table.insert(line[:-1])

print("Number of words in the dictionary =",hash_table._number_in_table)
print("Percent of hash table buckets used = ","{:.2f}".format(100.0 * hash_table._in_use / hash_table._size) + '%')
print("Average non-empty bucket size = ","{:.2f}".format(hash_table.average_non_empty_bucket_size()))
print("Largest bucket size =",hash_table.largest_bucket_size())

with open("ihaveadream.txt") as document:
    for line in document:
        words = line.split()
        for word in words:
            if not hash_table.find(Mystring(word)):
                print("Not found in the dictionary:",word)
