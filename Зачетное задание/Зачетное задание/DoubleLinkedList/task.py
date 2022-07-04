from collections.abc import MutableSequence

from typing import Any, Iterable, Optional

from node import Node

class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head




    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, item):
        pass

    def __len__(self):
        pass

    def insert(self, index: int, value: Any) -> None:
        pass


class DoubleLinkedList(LinkedList):
        ...


if __name__ == '__main__':
    print(dir(MutableSequence))
    ...
