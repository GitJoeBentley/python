from mystring import Mystring      

class Node:
    def __init__(self, item = None, next = None):
        self._data = item
        self._next = next
        
    def __repr__(self):
        return self._data


class Linked_List:
    def __init__(self):
        self._top = None
        self._len = 0

    def push(self, item):
        temp = Node(item, self._top)
        self._top = temp
        self._len += 1

    def __contains__(self, item) -> bool:
        temp = self._top
        while temp:
            if temp._data == item:
                return True
            temp = temp._next
        return False
