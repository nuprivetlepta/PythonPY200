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

    "Как мне сделать сеттер, который будет брать тип из своего класса, а не хардкод?"
    # @classmethod
    # @next.setter
    # def next(cls, node_: Optional["cls"] = None):
    #     cls.is_valid(node_)
    #     cls._next = node_


class DoubleLinkedNode(Node):
    def __init__(self, value, next_=None, prev=None):
        super().__init__(value, next_)
        self._prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node_: Optional["DoubleLinkedNode"] = None):
        self.is_valid(node_)
        self._prev = node_

    def __repr__(self):
        next_repr: str = str(None) \
            if self.next is None \
            else f"DoubleLinkedNode({self.next.value}, {None}, {None})"
        prev_repr: str = str(None) \
            if self.prev is None \
            else f"DoubleLinkedNode({self.prev.value}, {None}, {None})"
        return f"DoubleLinkedNode({self.value}, {next_repr}, {prev_repr})"

    def __str__(self):
        return super().__str__()


if __name__ == "__main__":
    ...
