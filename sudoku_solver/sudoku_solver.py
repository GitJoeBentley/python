#!/usr/bin/python3

""" Recursively finds a solution for the unsolved inputted sudoku puzzle """
__author__ = 'Joe Bentley'

from collections.abc import Sequence
import sys

class Grid:
    def __init__(self, grid: Sequence[Sequence[str]]):
        self._grid = []
        for r in range(9):
            row = []
            for c in grid[r]:
                if c == ' ':
                    row.append(0)
                else:
                    row.append(int(c))           
            self._grid.append(row)
        
    def __repr__(self):
        # Draw top line
        s = '\u250f'
        for i in range(35):
            if i == 11 or i == 23:
                s = s + '\u2533'
            elif i == 3 or i == 7  or i == 15 or i == 19 or i == 27 or i == 31:
                s = s + '\u252F'
            else:
                s = s + '\u2501'
        s = s + '\u2513\n'
        for r in range(9):
            s = s + '\u2503'
            for col in range(9):
                ch = str(self._grid[r][col]) if self._grid[r][col] else ' '
                s = s + ' ' + ch + ' '
                # vertical divider lines
                if col % 3 ==2:
                    s = s + '\u2503'
                else:
                    s = s + '\u2502'
            if r == 2 or r == 5:
                # Heavy horizontal line
                s = s + '\n' + '\u2523'
                for i in range(35):
                    if i == 11 or i == 23:
                        s = s + '\u254B'
                    elif i == 3 or i == 7  or i == 15 or i == 19 or i == 27 or i == 31:
                        s = s + '\u253F'
                    else:    
                        s = s + '\u2501'
                s = s + '\u252b\n'
            elif r % 3 != 2:
                # Light horizontal line
                s = s + '\n\u2520'
                for i in range(35):
                    if i == 11 or i == 23:
                        s = s + '\u2542'
                    elif i == 3 or i == 7  or i == 15 or i == 19 or i == 27 or i == 31:
                        s = s + '\u253C'
                    else:                    
                        s = s + '\u2500'
                s = s + '\u2528\n'
            else:
                # Bottom Line
                s = s + '\n\u2517'
                for i in range(35):
                    if i == 11 or i == 23:
                        s = s + '\u253B'
                    elif i == 3 or i == 7  or i == 15 or i == 19 or i == 27 or i == 31:
                        s = s + '\u2537'
                    else:    
                        s = s + '\u2501'
                s = s + '\u251B\n'
        return s

    
    # returns True if value is not in row
    def check_row(self, row: int, value: str) -> bool:
        return not value in self._grid[row]

    # returns True if value is not in column
    def check_column(self, column: int, value: str) -> bool:
        for row in range(9):
            if self._grid[row][column]  == value:
                return False
        return True
    
    # returns True if value is not in block
    def check_block(self, row: int, column: int, value) -> bool:
        if row > 5:
            min_row = 6
        elif row > 2:
            min_row = 3
        else:
            min_row = 0
        if column > 5:
            min_col = 6
        elif column > 2:
            min_col = 3
        else:
            min_col = 0
        for r in range(min_row, min_row + 3):
            for c in range(min_col, min_col + 3):
                if self._grid[r][c] == value:
                    return False
        return True
    
    def check_position(self, row: int, col: int, value: str) -> bool:
        if self._grid[row][col] == ' ':
            if self.check_row(row, value):
                if self.check_column(col, value):
                    if self.check_block(row, col, value):
                        return True
        return False
    
    def solve(self) -> []:
        for row in range(9):
            for col in range(9):
                for val in range(1, 10):
                    value = str(val)
                    test_grid = self._grid[:]
                    if self.check_position(row, col, value):
                        test_grid[row][col] = value
                        print(Grid(test_grid))
                        return test_grid
                    
            


if __name__ == '__main__':
    fin = open("puzzle1.txt", "r")
    original = [line.rstrip().ljust(9) for line in fin]
    grid = Grid(original)
    print(grid)
    #grid.solve()
        
    