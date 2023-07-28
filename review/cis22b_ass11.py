#!/usr/bin/python3

import urllib.request
from math import sqrt
import abc
from abc import ABC

"""
This python module is a solution for the CIS22 assignment 11 located at 
http://voyager.deanza.edu/~bentley/cis22b/ass11.html
"""

__author__ = "Joe Bentley, joe.deanza@gmail.com"

class Quadrilateral(ABC):
    def __init__(self, a: float,  b: float, c: float, d: float):
        self._sides = (a, b, c, d)

    def perimeter(self) -> float:
        return self._sides[0] + self._sides[1] + self._sides[2] + self._sides[3]

    def __repr__(self) -> str:
        return (type(self).__name__ + ':').ljust(20) + 'sides:' + \
            '{:5.1f}{:5.1f}{:5.1f}{:5.1f}'. \
                format(self._sides[0],self._sides[1],self._sides[2],self._sides[3]) + \
                    '  area:' + '{:6.2f}'.format(self.area()) + \
                        '  perimeter:' + '{:6.1f}'.format(self.perimeter())

    @abc.abstractmethod
    def area(self):
        pass


class Kite(Quadrilateral):
    def __init__(self, side1, side2, diagonal):
        super().__init__(side1, side2, side2, side1)
        self._p = diagonal

    def area(self) -> float:
        return 0.5 * self._p * (sqrt(self._sides[0] * self._sides[0] - (self._p / 2) * (self._p / 2)) +
                                sqrt(self._sides[1] * self._sides[1] - (self._p / 2) * (self._p/2)))
        

class Rectangle(Quadrilateral):
    def __init__(self, side1, side2):
        super().__init__(side1, side2, side1, side2)

    def area(self) -> float:
        return self._sides[0] * self._sides[1]


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Trapezoid(Quadrilateral):
    def __init__(self, a: float,  b: float, c: float, d: float, height=None):
        super().__init__(a, b, c, d)
        if height:
            self._height = height
        else:
            self._height = self._determine_height()

    def _determine_height(self) -> float:
        temp1 = (self._sides[0] + self._sides[1] - self._sides[2] + self._sides[3]) * \
        (-self._sides[0] + self._sides[1] + self._sides[2] + self._sides[3]) * \
        (self._sides[0] - self._sides[1] - self._sides[2] + self._sides[3]) * \
        (self._sides[0] + self._sides[1] - self._sides[2] - self._sides[3]);
        temp2 = 4 * (self._sides[0] - self._sides[2]) * (self._sides[0] - self._sides[2]);
        return sqrt( temp1 / temp2);

    def area(self):        
        return 0.5 * self._height * (self._sides[0] + self._sides[2])


class IsoscelesTrapezoid(Trapezoid):
    def __init__(self, a: float,  b: float, c: float):
        super().__init__(a, b, c, b)


class Parallelogram(Trapezoid):
    def __init__(self, a: float, b: float, height: float):
        super().__init__(a, b, a, b, height)


class Rhombus(Parallelogram):
    def __init__(self, a: float, height: float):
        super().__init__(a, a, height)


if __name__ == '__main__':
    file = urllib.request.urlopen('http://voyager.deanza.edu/~bentley/cis22b/ass11data.txt').read().decode().split('\r\n')
    for line in file:
        data = line.split()
        if len(data) < 1:
            break
        match data[0]:
            case 'ki':
                q = Kite(float(data[1]),float(data[2]),float(data[3]))
            case 'tr':
                q = Trapezoid(float(data[1]),float(data[2]),float(data[3]),float(data[4]))
            case 'it':
                q = IsoscelesTrapezoid(float(data[1]),float(data[2]),float(data[3]))
            case 'pa':
                q = Parallelogram(float(data[1]),float(data[2]),float(data[3]))
            case 'rh':
                q = Rhombus(float(data[1]),float(data[2]))
            case 're':
                q = Rectangle(float(data[1]),float(data[2]))
            case 'sq':
                q = Square(float(data[1]))
        print(q)
