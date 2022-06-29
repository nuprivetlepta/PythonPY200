from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.__next = next_
    #
    # @classmethod
    # def is_valid(cls):
    #     if not isinstance(cls, (type(None), type(cls))):
    #         raise TypeError

    @staticmethod
    def is_valid(smth):
        if not isinstance(smth, (type(None), Node)):
            raise TypeError

    def __str__(self) -> str:
        return f"{self.value}, {self.__next}"

    def __repr__(self):
        return f"Node({self.value}, {self.__next})"

    @property
    def get_next(self):
        self.is_valid(self.__next)
        return self.__next

    @get_next.setter
    def get_next(self, next_: Optional["Node"] = None):
        self.is_valid(next_)
        self.__next = next_


class DoubleLinkedNode(Node):
    ...


if __name__ == "__main__":
    node = Node(1, Node(2))
    node.get_next = Node(15, None)
    print(node.get_next)
    print(node)

