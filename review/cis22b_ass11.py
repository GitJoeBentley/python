#!/usr/bin/python3

from math import sqrt
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
        return self._a + self._b + self._c + self._d
    
    def __repr__(self) -> str:
        return (type(self).__name__ + ':').ljust(20) + 'sides:' + str(self.area())
    
    @classmethod
    def area(self):
        pass

class Kite(Quadrilateral):
    def __init__(self, side1, side2, diagonal):
        super().__init__(side1, side2, side2, side1)

    def area(self) -> float:
        return 54
    
k= Kite(2,3,1)
print(k)

