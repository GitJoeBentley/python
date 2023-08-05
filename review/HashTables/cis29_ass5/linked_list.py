from mystring import Mystring      

class Node:
    def __init__(self, item = None, next = None):
        self._data = item
        self._next = next


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
        while temp != None:
            if temp._data == item:
                return True
            temp = temp._next
        return False

    def __iter__(self):
        temp = self._top
        while temp:
            node = temp._next
            temp = temp._next
            yield node
        
    """
    def print(self):
        temp = self._top
        while temp != None:
            temp = temp._next
    """
