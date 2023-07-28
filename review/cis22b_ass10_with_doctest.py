#1/usr/bin/python3

from math import pi
from math import sqrt

"""
This python module is a solution for the CIS22 assignment 10 located at 
http://voyager.deanza.edu/~bentley/cis22b/ass10.html
"""

__author__ = "Joe Bentley, joe.deanza@gmail.com"


class Location:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return '({:.2f},{:.2f})'.format(self._x,self._y)        


class Shape:
    def __init__(self, x, y, color: str):
        """
        Constructs a shape object
        >>> sh = Shape(4,5,"red")
        >>> sh
        Shape     red            (4.00,5.00)  area = n/a
        """
        self._location = Location(x, y)
        self._color = color

    def area(self):
        return None

    def _area_as_str(self) -> str:
        area = self.area()
        return '{:.2f}'.format(area) if area else 'n/a'

    def __repr__(self) -> str:
        return type(self).__name__.ljust(10) + self._color.ljust(15) + str(self._location) + "  area = " + self._area_as_str()
    

class Square(Shape):
    def __init__(self, x, y, side, color):
        """
        Creates a Square object
        >>> sq1 = Square(1.0,2.0,3.1,"green")
        >>> sq1
        Square    green          (1.00,2.00)  area = 9.61
        """
        super().__init__(x, y, color)
        self._side = side

    def area(self) -> float:
        return self._side * self._side


class Circle(Shape):
    def __init__(self, x, y, radius, color):
        """
        Creates a Circle object
        >>> c1 = Circle(0.0,2.0,3.4,"blue")
        >>> c1
        Circle    blue           (0.00,2.00)  area = 36.32
        >>> c1.area()
        36.32
        >>> c1._area_as_str()
        '36.32'
        """
        super().__init__(x, y, color)
        self._radius = radius

    def area(self) -> float:
        return pi * self._radius * self._radius


class Triangle(Shape):
    def __init__(self, x, y, s1, s2, s3, color):
        """
        Creates a Triangle object
        >>> t1 = Triangle(1.4,2.0,1.1,1.2,1.3,"red")
        >>> t1
        Triangle  red            (1.40,2.00)  area = 0.61
        """
        super().__init__(x, y, color)
        self._a = s1
        self._b = s2
        self._c = s3

    def area(self) -> float:
        s = (self._a + self._b + self._c) / 2
        return sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))



if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""
    sh = Shape(4,5,"red")
    print(sh,'\n')

    sq1 = Square(1.0,2.0,3.1,"green")
    print(sq1)
    sq2 = Square(1.5,2.5,3.2,"lime green")
    print(sq2)
    sq3 = Square(6.7,0.0,3.3,"chartreuse")
    print(sq3)
    print('')

    c1 = Circle(0.0,2.0,3.4,"blue")
    print(c1)
    c2 = Circle(0.0,2.0,3.5,"peacock blue")
    print(c2)
    c3 = Circle(0.0,2.0,3.6,"sapphire")
    print(c3)
    print('')

    t1 = Triangle(1.4,2.0,1.1,1.2,1.3,"red")
    print(t1)
    t2 = Triangle(1.23,2.0,3,4,5,"cardinal red")
    print(t2)
    t3 = Triangle(4.56,2.75,1,1,1,"crimson")
    print(t3)
"""