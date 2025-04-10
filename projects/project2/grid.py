#Grid.py
from datastructurescopy.array2d import Array2D
from cell import Cell
import copy
import random

class Grid:
    def __init__(self, number_of_rows, number_of_cols) -> None:
        self.number_of_rows = number_of_rows
        self.number_of_cols = number_of_cols
        self.starting_sequence = [[Cell() for i in range(self.number_of_cols)] for i in range(self.number_of_rows)]
        self.grid = Array2D(self.starting_sequence, Cell)
    
    def next_gen(self) -> Array2D:
        """create new grid and stores the previous grid"""
        self.new_grid = copy.deepcopy(self)
        self.original_grid = self
        #insert new grid changes functions here
        for row in range(self.original_grid.number_of_rows):  
            for col in range(self.original_grid.number_of_cols):
                if self.original_grid.grid[row][col].neighbor_count in [0,1,4,5,6,7,8]:
                    #CELL DIES
                    self.new_grid.grid[row][col].alive_status = False
                elif self.original_grid.grid[row][col].neighbor_count == 3:
                    #CELL IS BORN. REJOICE
                    self.new_grid.grid[row][col].alive_status = True
        return self.new_grid
    
    def check_for_change(self, other_grid) -> bool:
        """Returns true if change between grids"""
        for row in range(self.number_of_rows):  
            for col in range(self.number_of_cols): 
                if self.grid[row][col].alive_status != other_grid.grid[row][col].alive_status:
                    return True
        return False

    def display(self):
        """displays the grid"""
        for row in range(self.number_of_rows):
            print(self.grid[row])

    def neighbor_detection(self, cell):
        """Detects how many neighbors are around a cell and stores it."""
        y = cell.position_row
        x = cell.position_col
        cell.neighbor_count = 0

        # 3 spaces in the row above
        if y != 0:
            if x not in [0, self.number_of_cols - 1]: 
                for i in range(3):
                    if self.grid[y-1][x-1+i].alive_status:
                        cell.neighbor_count += 1
            elif x == 0:
                for i in range(2):
                    if self.grid[y-1][x+i].alive_status:
                        cell.neighbor_count += 1
            elif x == self.number_of_cols - 1:  
                for i in range(2):
                    if self.grid[y-1][x-1+i].alive_status:
                        cell.neighbor_count += 1

        # 2 spaces to the left and right of the current row
        if x not in [0, self.number_of_cols - 1]:  
            if self.grid[y][x-1].alive_status:
                cell.neighbor_count += 1
            if self.grid[y][x+1].alive_status:
                cell.neighbor_count += 1
        elif x == 0:
            if self.grid[y][x+1].alive_status:
                cell.neighbor_count += 1
        elif x == self.number_of_cols - 1:  
            if self.grid[y][x-1].alive_status:
                cell.neighbor_count += 1

        # 3 spaces in the row below
        if y != self.number_of_rows - 1:  
            if x not in [0, self.number_of_cols - 1]:  
                for i in range(3):
                    if self.grid[y+1][x-1+i].alive_status:
                        cell.neighbor_count += 1
            elif x == 0:
                for i in range(2):
                    if self.grid[y+1][x+i].alive_status:
                        cell.neighbor_count += 1
            elif x == self.number_of_cols - 1:  
                for i in range(2):
                    if self.grid[y+1][x-1+i].alive_status:
                        cell.neighbor_count += 1
            







