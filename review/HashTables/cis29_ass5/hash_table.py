from mystring import Mystring
from linked_list import Linked_List, Node

class DuplicateError(Exception):
    def __init__(self, word):
        self._word = word

    def __str__(self):
        return "Duplicate Mystring: " + self._word 


class Hash_table:
    def __init__(self):
        self._size = 2000
        self._in_use = 0
        self._array = [Linked_List() for i in range(self._size)]
        self._number_in_table = 0

    def insert(self, s):
        my_s = Mystring(s)
        index = my_s._hash % self._size
        if self._array[index]._len == 0:
            self._in_use  += 1
        try:
            if self._array[index].__contains__(s):
                raise(DuplicateError(s))
            self._array[index].push(my_s)
            self._number_in_table += 1
        except DuplicateError as e:
            print(e)

    #def print(self):
    #    for index in range(self._size):
    #        self._array[index].print()

    def average_non_empty_bucket_size(self):
        size = 0
        count_buckets = 0
        for index in range(self._size):
            if self._array[index]._len:
                size += self._array[index]._len
                count_buckets += 1
        return size / count_buckets
    
    def largest_bucket_size(self):
        size = 0
        for index in range(self._size):
            if self._array[index]._len > size:
                size = self._array[index]._len
        return size

    def __contains__(self, myword):
        return myword in self._array[myword._hash % self._size]
