#!/usr/bin/python3

"""
This module is a python solution for the CIS29 Example 8-3
http://voyager.deanza.edu/~bentley/cis29/examples/ex8-3.cpp
"""

__author__ = "Joe Bentley, joe.deanza@gmail.com"

def printBits(text, value, num_bits = 8):
    svalue = str(value)
    if num_bits == 8:
        print(text.ljust(4) + '='+svalue.rjust(5),'{0:08b}'.format(value))
    else:
        bdata = '{0:032b}'.format(value)
        bdata = bdata[0:8] + ' ' + bdata[8:16] + ' ' + bdata[16:24]+ ' ' + bdata[24:32]
        print(text.ljust(4) + '=' + svalue.rjust(5), bdata)

a = 77
b = 20

printBits('a',a)
printBits('b',b)
printBits('a&b',a&b,32)
printBits('a|b',a|b,32)
printBits('a^b',a^b,32)
printBits('~a',~a,32)
printBits('a<<1',a<<1,32)
printBits('a<<2',a<<2,32)
printBits('a<<8',a<<8,32)
printBits('a<<9',a<<9,32)
printBits('a>>1',a>>1,32)
printBits('a>>2',a>>2,32)
printBits('a>>9',a>>9,32)
