import os

from datastructurescopy.array import Array, T
from datastructurescopy.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        self.max_size = max_size
        self.data_type = data_type
        self.default = data_type()
        starting_sequence = [data_type() for i in range(max_size)]
        self.stack = Array(starting_sequence, data_type)
        self._top = 0

    def push(self, item: T) -> None:
        """top = top + 1"""
        self.stack[self._top] = item
        self._top += 1

    def pop(self) -> T:
        if self._top == 0: 
            raise IndexError

        self._top -= 1
        item = self.stack[self._top]
        self.stack[self._top] = self.default
        return item

    def clear(self) -> None:
        self.stack = Array([self.default] * self.max_size, self.data_type)  # Reset storage
        self._top = 0 
       
    @property
    def peek(self) -> T:
        return self.stack[self._top-1] 

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self.max_size
    
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        return self.max_size == self._top

    @property
    def empty(self) -> bool:
        return self._top == 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ArrayStack) or len(self) != len(other):
            return False
    
        for i in range(self._top):
            if self.stack[i] != other.stack[i]:
                return False
        return True
            

    def __len__(self) -> int:
        return self._top
    
    def __contains__(self, item: T) -> bool:
        for i in range(len(self.stack)):
           if self.stack[i] == item:
               return True
        else:
           return False

    def __str__(self) -> str:
        return str([self.stack[i] for i in range(self._top)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    my_stack = ArrayStack(5, int)
    print(my_stack.stack)