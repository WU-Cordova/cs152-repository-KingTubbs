from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self._contents = []
        self._count = {}

    def add(self, item: T) -> None:
        if item == None:
            raise TypeError
        elif item in self._contents:
            #count goes up
            self._contents.append(item)
            self._count[item] += 1
        elif item not in self._contents:
            #count goes to 1
            self._contents.append(item)
            self._count[item] = 1
    def remove(self, item: T) -> None:
        if item not in self._contents:
            raise ValueError
        elif item in self._contents:
            self._count[item] -= 1

    def count(self, item: T) -> int:
        if item not in self._contents:
            return 0
        else:
            return self._count[item]

    def __len__(self) -> int:
        return len(self._contents)

    def distinct_items(self) -> int:
        unique_items = []
        for item in self._contents:
            if item not in unique_items:
                unique_items.append(item)
            else:
                pass
        return unique_items

    def __contains__(self, item) -> bool:
        if item in self._contents:
            return True
        elif item not in self._contents:
            return False

    def clear(self) -> None:
        self._contents.clear()
        self._count.clear()

if __name__ == "__main__":
    bagtest = Bag()
    bagtest.add(4)
    bagtest.add(4)
    bagtest.add(5)
    