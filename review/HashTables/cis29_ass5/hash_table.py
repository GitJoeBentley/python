from mystring import Mystring
from linked_list import Linked_List, Node
from config import hash_table_size


class DuplicateError(Exception):
    def __init__(self, word):
        self._word = word

    def __str__(self):
        return "Duplicate Mystring: " + self._word 


class Hash_table:
    def __init__(self):
        self._in_use = 0
        self._array = [Linked_List() for i in range(hash_table_size)]
        self._number_in_table = 0
    """
    def __setitem__(self, index, s):
        if self._array[index]._len == 0:
            self._in_use  += 1
            print( self._in_use)
        try:
            if self._array[index].__contains__(s):
                raise(DuplicateError(s))
            self._array[index].push(my_s)
            self._number_in_table += 1
        except DuplicateError as e:
            print(e)
    """
    def __getitem__(self, index):
        return self._array[index]

    def average_non_empty_bucket_size(self):
        size = 0
        count_buckets = 0
        for index in range(hash_table_size):
            if self._array[index]._len:
                size += self._array[index]._len
                count_buckets += 1
        return size / count_buckets
    
    def largest_bucket_size(self):
        size = 0
        for index in range(hash_table_size):
            if self._array[index]._len > size:
                size = self._array[index]._len
        return size

    def __contains__(self, myword):
        index = hash(myword) 
        return myword in self._array[index]
    
    def __len__(self):
        return sum([len(bucket) for bucket in self._array if bucket])
    
    def number_of_buckets_in_use(self):
        return sum([1 for bucket in self._array if bucket])
