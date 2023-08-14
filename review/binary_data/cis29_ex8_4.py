#!/usr/bin/python3

"""
This module is a python solution for the CIS29 Example 8-4
http://voyager.deanza.edu/~bentley/cis29/examples/ex8-4.cpp
"""

__author__ = "Joe Bentley, joe.deanza@gmail.com"
      
def printBits(text, num_bits = 8):
    expr = text.ljust(7)
    if '|=' in text or '^=' in text:
        text = text.replace('=','')
    value = eval(text)
    svalue = str(value)
    if num_bits == 8:
        print(expr + '='+svalue.rjust(5),'{0:08b}'.format(value))
    else:
        bdata = '{0:032b}'.format(value)
        bdata = bdata[0:8] + ' ' + bdata[8:16] + ' ' + bdata[16:24]+ ' ' + bdata[24:32]
        print(expr + '=' + svalue.rjust(5), bdata)
        
# turn a bit on
a = 34
printBits('a')
b = 4
printBits('b')
printBits('a |= b')
print('')

# turn a bit off
a = 34
printBits('a')
b = 2
printBits('b')
printBits('a &~ b', 32)
print('')

# toggle a bit
a = 34
printBits('a')
b = 66
printBits('b')
printBits('a ^= b')
print('')

# test to see if a bit is turned on
a = 34
printBits('a')
printBits('2')
printBits('a & 2')


