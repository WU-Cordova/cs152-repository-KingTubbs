# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


from datastructurescopy.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        self.starting_sequence = starting_sequence
        self.data_type = data_type
        if not isinstance(starting_sequence, Sequence):
            raise ValueError
        if not isinstance(data_type, type):
            raise ValueError
        for item in starting_sequence:
            if not isinstance(item, self.data_type):
                raise TypeError
        self.__items = list(starting_sequence) 
        self.__item_count = len(self.__items) 
        self.__data_type = data_type


    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, slice):
            return Array(self.__items[index])  
        if self.__item_count <= index:
            raise IndexError
        if not isinstance(index, int):
            raise TypeError
        return self.__items[index]
    
    def __setitem__(self, index: int, item: T) -> None:
        if self.__item_count < index:
            raise IndexError
        if not isinstance(item, self.data_type):
            raise TypeError
        self.__items[index] = item

    def append(self, data: T) -> None:
        if self.__item_count == len(self.__items):
            new_physical_size = max(1, 2 * len(self.__items))
            new_items = [None] * new_physical_size
            for i in range(len(self.__items)):
                new_items[i] = self.__items[i]
            self.__items = new_items
        self.__items[self.__item_count] = data
        self.__item_count += 1        

    def append_front(self, data: T) -> None:
        if self.__item_count == len(self.__items):
            new_physical_size = max(1, 2 * len(self.__items))
            new_items = [None] * new_physical_size
            for i in range(self.__item_count):
                new_items[i+1] = self.__items[i]
            self.__items = new_items
        else: 
            for i in range(self.__item_count, 0, -1):
                self.__items[i] = self.__items[i-1]
        self.__items[0] = data
        self.__item_count += 1  

    def pop(self) -> None:
        self.__items[-1] = None
        self.__item_count -= 1
        if self.__item_count <= len(self.__items)/4:
            new_physical_size = max(1, len(self.__items) // 2)
            new_items = [None] * new_physical_size
            for i in range(self.__item_count):
                new_items[i] = self.__items[i]
            self.__items = new_items
    
    def pop_front(self) -> None:
        if self.__item_count == 0:
            raise IndexError
        for i in range(1, self.__item_count):
            self.__items[i-1] = self.__items[i]
        self.__item_count -= 1
        self.__items[self.__item_count] = None
        if self.__item_count <= len(self.__items) // 4:
            new_physical_size = max(1, len(self.__items) // 2)
            new_items = [None] * new_physical_size
            for i in range(self.__item_count):
                new_items[i] = self.__items[i]
            self.__items = new_items

    def __len__(self) -> int: 
        return self.__item_count

    def __eq__(self, other: object) -> bool:
        #works
        if not isinstance(other, Array):
            return False
        if self.__items == other.__items and self.data_type == other.data_type:
            return True
        else:
            return False
    
    def __iter__(self) -> Iterator[T]:
        for i in range(self.__item_count):
            yield self.__items[i]

    def __reversed__(self) -> Iterator[T]:
        reverse = self.starting_sequence[-1:]
        for i in reverse:
            yield self.__items[i]

    def __delitem__(self, index: int) -> None:
        #works
        del self.__items[index]
        self.__item_count -= 1
        

    def __contains__(self, item: Any) -> bool: 
        #works
        for i in self.__items:
            if item == i:
                return True
        return False

    def clear(self) -> None:
        self.__items = [None] * self.__item_count  
        self.__item_count = 0  

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    print("hi")