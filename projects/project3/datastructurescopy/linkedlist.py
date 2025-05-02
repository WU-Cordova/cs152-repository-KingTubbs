from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructurescopy.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self._data_type = data_type
        self._head = None
        self._tail = None
        self.size = 0

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        linked_list = LinkedList(data_type)
        for i in sequence:
            linked_list.append(i)
        return linked_list

    def append(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item datatype is not consistent")
        
        new_node = self.Node(item)

        if self._head == None:
            """list is empty, first item means head and tail same"""
            self._head = new_node
            self._tail = self._head
        else:
            """list has at least one element, 
            python remembers an object if something is refering to it"""
            new_node.previous = self._tail
            self._tail.next = new_node
            self._tail = new_node
        
        self.size += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item datatype is not consistent")
        
        new_node = self.Node(item)

        if self._head == None:
            """list is empty"""
            self._head = new_node
            self._tail = self._head
        else:
            """list has at lease one element"""
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node
        
        self.size += 1

    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(item, self._data_type) or not isinstance(target, self._data_type):
            raise TypeError("Item and target are not the same data type")

        current_node = self._head
        while current_node:
            if current_node.data == target:
                break
            current_node = current_node.next
        
        if current_node is None:
            raise ValueError(f"Target not found in the list")

        new_node = self.Node(item)
        
        if current_node == self._head:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node
        else:
            new_node.previous = current_node.previous
            new_node.next = current_node
            current_node.previous.next = new_node
            current_node.previous = new_node        

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(item, self._data_type) or not isinstance(target, self._data_type):
            raise TypeError("Item and target are not the same data type")

        current_node = self._head
        while current_node:
            if current_node.data == target:
                break
            current_node = current_node.next
        
        if current_node is None:
            raise ValueError(f"Target not found in the list")
        
        new_node = self.Node(item)
        
        if current_node == self._tail:
            new_node.previous = self._tail
            self._tail.next = new_node
            self._tail = new_node
        else:
            new_node.previous = current_node
            new_node.next = current_node.next
            current_node.next.previous = new_node
            current_node.next = new_node

    def remove(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item datatype is not consistent")

        if self._head is None:
            raise ValueError("Item not found")

        current_node = self._head
        while current_node:
            if current_node.data == item:
                self.size -= 1
                if current_node == self._head:
                    #If head
                    self._head = current_node.next
                    if self._head:  
                        self._head.previous = None
                    else:
                        self._tail = None  
                elif current_node == self._tail:
                    #If tail
                    self._tail = current_node.previous
                    self._tail.next = None
                else:
                    #In the middle
                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
                return  
            
            current_node = current_node.next

        raise ValueError("Item not found")
    
        

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item datatype is not consistent")
        
        if self._head is None:
            raise ValueError("Item not found")
        found_flag = False

        current_node = self._head
        while current_node:
            if current_node.data == item:
                found_flag = True
                self.size -= 1
                if current_node == self._head:
                    #If head
                    self._head = current_node.next
                    if self._head:  
                        self._head.previous = None
                    else:
                        self._tail = None  
                elif current_node == self._tail:
                    #If tail
                    self._tail = current_node.previous
                    self._tail.next = None
                else:
                    #In the middle
                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
            
            current_node = current_node.next

        if not found_flag:
            raise ValueError("Item not found")

    def pop(self) -> T:
        if self._head is None:
            raise IndexError("List is empty")
        
        popped_data = self._tail.data
        self.size -= 1

        if self._head == self._tail:
            #Only one element 
            self._head = None
            self._tail = None

        else:
            #otherwise
            self._tail = self._tail.previous
            self._tail.next = None

        return popped_data

    def pop_front(self) -> T:
        if self._head is None:
            raise IndexError("List is empty")
        
        popped_data = self._head.data
        self.size -= 1

        if self._head == self._tail:
            #Only one element 
            self._head = None
            self._tail = None

        else:
            #otherwise
            self._head = self._head.next
            self._head.previous = None

        return popped_data

    @property
    def front(self) -> T:
        if self._head is None:
            raise IndexError
        return self._head.data

    @property
    def back(self) -> T:
        if self._head is None:
            raise IndexError
        return self._tail.data

    @property
    def empty(self) -> bool:
        if self._head is None:
            return True
        else:
            return False

    def __len__(self) -> int:
        return self.size

    def clear(self) -> None:
        self._head = None  
        self._tail = None  
        self.size = 0      

    def __contains__(self, item: T) -> bool:
        current_node = self._head
        while current_node:
            if item == current_node.data:
                return True
            current_node = current_node.next
        return False

    def __iter__(self) -> ILinkedList[T]:
        self._current_node = self._head  
        return self  

    def __next__(self) -> T:
        if self._current_node is None:
            raise StopIteration  
        data = self._current_node.data  
        self._current_node = self._current_node.next  
        return data
    def __reversed__(self) -> ILinkedList[T]:
        reversed_list = LinkedList(self._data_type)
        current_node = self._tail

        while current_node:
            reversed_list.append(current_node.data)
            current_node = current_node.previous
        
        return reversed_list

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False  
        
        if len(self) != len(other):
            return False
        
        current_node = self._head
        other_node = other._head
        
        while current_node:
            if current_node.data != other_node.data:
                return False 
            current_node = current_node.next
            other_node = other_node.next
        return True  
    
    def __str__(self) -> str:
        items = []
        current = self._head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
