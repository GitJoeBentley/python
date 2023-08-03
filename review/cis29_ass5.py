"""
CIS29 Assignment 3 - Python version
"""

import os
import ctypes

def print_column_data_in_hex(data: list[int], width: int, num_columns: int):
    print("")
    width_fmt = "{:>" + str(width) + "}"
    for i in range(1, len(data) + 1):
        print(width_fmt.format(hex(data[i - 1])),end="")
        if i % num_columns == 0:
            print("")


filename = "ass3data.bin"

size = os.stat(filename).st_size
print("The file size is",size,"bytes")
num_ints = int(size / 4)
print("The file contains",num_ints,"ints")


with open(filename, 'rb') as file:
    raw_int_data = [int.from_bytes(file.read(4), byteorder='little') for i in range(num_ints)]
    int_data = [ctypes.c_long(i & 0xffffffff).value for i in raw_int_data]

    for i in range(1, num_ints + 1):
        print("{:>12}".format(int_data[i - 1]),end="")
        if i%6 == 0:
            print("")
            
    print_column_data_in_hex(raw_int_data, 12, 6)

    for i in range(num_ints):
        raw_int_data[i] = raw_int_data[i] ^ 0x00ffff00
    print_column_data_in_hex(raw_int_data, 12, 6)

    # Extract the 2rd byte of each int and display it in hexadecimal, with a width of 6, twelve to a line.
    for i in range(num_ints):
        raw_int_data[i] = (raw_int_data[i] & 0x00ff0000) >> 16
    print_column_data_in_hex(raw_int_data, 6, 12)

    # Reverse (flip) the nibbles of  the resulting byte and display it in hexadecimal, with a width of 6, twelve to a line.
    for i in range(num_ints):
        nibble1 = (0xf0 & raw_int_data[i]) >> 4;
        nibble2 = (0x0f & raw_int_data[i]);
        raw_int_data[i] = nibble1 + (nibble2 << 4);
    print_column_data_in_hex(raw_int_data, 6, 12)

    for i in range(num_ints):
        print(chr(int(hex(raw_int_data[i])[2:])+32),end="")
