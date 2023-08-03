from mystring import Mystring      

class Node:
    def __init__(self, item = None, next = None):
        self._data = item
        self._next = next


class Linked_List:
    def __init__(self):
        self._top = None
        self._len = 0
        

    def print(self):
        temp = self._top
        while temp != None:
            temp = temp._next

    def push(self, item):
        temp = Node(item, self._top)
        self._top = temp
        self._len += 1

    def find(self, item):
        temp = self._top
        if item[:2] == 'ag':
            print("item=",item," _len=",self._len)
        self.print()
        while temp != None:
            #print("30:",temp._data,temp)
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
        
