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
        return f"{self.value}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value}, {repr(self._next)})"

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
