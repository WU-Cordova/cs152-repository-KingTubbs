from datastructures.array2d import Array2D

class Grid:
    def __init__(self, number_of_rows, number_of_cols) -> None:
        self.number_of_rows = number_of_rows
        self.number_of_cols = number_of_cols
        starting_sequence = [bool for i in range(self.number_of_cols) for i in range(self.number_of_rows)]
        grid = Array2D(starting_sequence, bool)


    
    def new_grid(self, original_grid):
        #original grid is original array2d

