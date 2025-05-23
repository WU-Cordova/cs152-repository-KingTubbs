#array2d.py
from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructurescopy.iarray import IArray
from datastructurescopy.array import Array
from datastructurescopy.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns
            self.data_type = data_type

        def __getitem__(self, column_index: int) -> T:
            if not 0 <= column_index < self.num_columns:
                raise IndexError
            index = self.map_index(self.row_index, column_index)
            return self.array[index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            index = self.map_index(self.row_index, column_index)
            self.array[index] = value

        def map_index(self, row_index:int, column_index:int) -> int:
            return row_index * self.num_columns + column_index
        
        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index] #self = row object
        
        def __reversed__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[-column_index - 1]

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not (isinstance(starting_sequence, Sequence) and not isinstance(starting_sequence, (str, bytes))):
            raise ValueError("starting_sequence must be a sequence of sequences")

        if not all(isinstance(row, Sequence) and not isinstance(row, (str, bytes)) for row in starting_sequence):
            raise ValueError("starting_sequence must be a sequence of sequences")

        if len(starting_sequence) > 0 and not all(len(row) == len(starting_sequence[0]) for row in starting_sequence):
            raise ValueError("starting_sequence must be a sequence of sequences with the same length")

        if not all(isinstance(item, data_type) for row in starting_sequence for item in row):
            raise ValueError("All items must be of the same type")
    
        self.data_type = data_type
        self.starting_sequence = starting_sequence
        self.row_len = len(starting_sequence)
        self.column_len = len(starting_sequence[0])

        self.array2d = Array([data_type() for item in range(self.row_len * self.column_len)], data_type=data_type)

        index = 0
        for row_index in range(self.row_len):
            for column_index in range(self.column_len): #may need to check to see if length is same for indexes
                self.array2d[index] = starting_sequence[row_index][column_index]
                index += 1


    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        starting_sequence = []

        for row in range(rows):
            starting_sequence.append([]) #appending a list to list index?
            for col in range(cols):
                starting_sequence[row].append(data_type())

        return Array2D(starting_sequence=starting_sequence, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if not 0 <= row_index < self.row_len:
            raise IndexError
        return Array2D.Row(row_index, self.array2d, self.column_len, self.data_type)
        
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row_index in range(self.row_len):
            yield self[row_index]
    
    def __reversed__(self):
        for row_index in reversed(range(self.row_len)):
            yield self[row_index]
    
    def __len__(self): 
        return self.row_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.row_len} Rows x {self.column_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')