#!/usr/bin/python3

"""
This module is a python solution for the CIS29 Example 8-1
http://voyager.deanza.edu/~bentley/cis29/examples/ex8-1.cpp
"""

__author__ = "Joe Bentley, joe.deanza@gmail.com"

def printBits(value):
    if type(value).__name__ == 'str' and len(value) == 1:
        print(value.rjust(8),'=','{0:08b}'.format(ord(value)))
    else:
        svalue = str(value)
        print(svalue.rjust(8),'=','{0:08b}'.format(value))
    
printBits('A');
printBits(12)
printBits(32000)
printBits(25)
printBits(255)
printBits(1234)
printBits(123456)
printBits(12345678)
printBits(1234567890)
printBits(2147483647)
printBits(-2147483648)
