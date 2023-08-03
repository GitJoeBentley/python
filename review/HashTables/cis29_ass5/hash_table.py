from mystring import Mystring
from linked_list import Linked_List, Node

class DuplicateError(Exception):
    def __init__(self, word):
        self._word = word

    def __str__(self):
        return "Duplicate Mystring: " + self._word 


class Hash_table:
    def __init__(self):
        self._size = 8
        self._in_use = 0
        self._array = [Linked_List() for i in range(self._size)]
        self._number_in_table = 0

    def _resize(self):
        new_size = 3 * self._in_use
        self.print()
        print("Resize to new size",new_size)
        self._in_use = 0
        new_array = [Linked_List() for i in range(new_size)]
        for index in range(self._size):
            for word in self._array[index]:
                if word:
                    index = word._data._hash % new_size
                    #print("Re-Inserting",word._data._str,"into new array at index",index)
                    if new_array[index]._len == 0:
                        self._in_use  += 1
                    if word == "ago":
                        print("ago at index",index)
                    new_array[index].push(word._data)
        self._size = new_size
        self._array = new_array

    def insert(self, s: str):
        if self._in_use > .9 * self._size:
            self._resize()
        
        my_s = Mystring(s)
        index = my_s._hash % self._size
        if self._array[index]._len == 0:
            self._in_use  += 1
        try:
            if self._array[index].find(s):
                raise(DuplicateError(s))
            self._array[index].push(my_s)
            if my_s == "ago":
                print("ago at index",index)
            self._number_in_table += 1
        except DuplicateError as e:
            print(e)

    def print(self):
        for index in range(self._size):
            #print("Array index:",index)
            self._array[index].print()

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

    def find(self, myword):
        print(myword,myword._hash,myword._hash % self._size)
        return self._array[myword._hash % self._size].find(myword)
