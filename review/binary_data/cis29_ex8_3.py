#!/usr/bin/python3

def printBits(text, value, num_bits = 8):
    svalue = str(value)
    if num_bits == 8:
        print(text.ljust(4) + '='+svalue.rjust(5),'{0:08b}'.format(value))
    else:
        print(text.ljust(4) + '='+svalue.rjust(5),'{0:032b}'.format(value))

a = 77
b = 20

printBits('a',a)
printBits('b',b)
printBits('a&b',a&b,32)
printBits('a|b',a|b,32)
printBits('a^b',a^b,32)
