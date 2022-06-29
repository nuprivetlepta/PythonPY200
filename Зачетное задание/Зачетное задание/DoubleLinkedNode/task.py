from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self._next = next_

    @classmethod
    def is_valid(cls, node_):
        if not isinstance(node_, (type(None), cls)):
            raise TypeError

    def __str__(self) -> str:
        return f"{self.value}, {self._next}"

    def __repr__(self):
        return f"Node({self.value}, {repr(self._next)})"

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node_: Optional["Node"] = None):
        self.is_valid(node_)
        self._next = node_


class DoubleLinkedNode(Node):
    def __init__(self, value, next_, prev):
        super().__init__(value, next_)
        self.prev = prev


if __name__ == "__main__":
    node = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_2.next = node
    node_3.next = node_2
    print(node)
    print(repr(node))
    print(node_2)
    print(repr(node_2))
    print(node_3)
    print(repr(node_3))
