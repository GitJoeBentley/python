#1/usr/bin/python3

class Location:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __str__(self) -> str:
        return '({:.2f},{:.2f})'.format(self._x,self._y)
    
class Shape:
    def __init__(self, x, y, color: str):
        self._location = Location(x, y)
        self._color = color

    def __repr__(self) -> str:
        return type(self).__name__.ljust(10) + self._color.ljust(15) + str(self._location)

s = Shape(3,4,"blue")
print(s)