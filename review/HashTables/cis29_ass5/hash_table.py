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
        #self._in_use = 0
        self._array = [Linked_List() for i in range(hash_table_size)]

    def __getitem__(self, index: int):
        return self._array[index]

    def average_non_empty_bucket_size(self) -> float:
        total = 0
        count_buckets = 0
        for bucket in self._array:
            if bucket:
                total += len(bucket)
                count_buckets += 1            
        return total / count_buckets
    
    def largest_bucket_size(self):
        size = 0
        for bucket in self._array:
            size = max(size, len(bucket))
        return size

    def __contains__(self, myword): 
        return myword in self._array[hash(myword)]
    
    def __len__(self):
        return sum([len(bucket) for bucket in self._array if bucket])
    
    def number_of_buckets_in_use(self):
        return sum([1 for bucket in self._array if bucket])
