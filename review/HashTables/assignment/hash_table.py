from mystring import Mystring
from config import hash_table_size


class DuplicateError(Exception):
    def __init__(self, word):
        self._word = word

    def __str__(self):
        return "Duplicate Mystring: " + self._word 


class Hash_table:
    def __init__(self):
        self._array = [None for i in range(hash_table_size)]

    def add(self, item):
        index = hash(item)
        if not self._array[index]:
            self._array[index] = item
        else:
            while self._array[index]:
                if self._array[index] == item:
                    raise DuplicateError(item)
                index = index + 1 if index < hash_table_size - 1 else 0
            self._array[index] = item

    def __contains__(self, item) -> bool:
        index = hash(item)
        while self._array[index] and self._array[index] != item:
            index = index + 1 if index < hash_table_size - 1 else 0
        return self._array[index] == item
                    