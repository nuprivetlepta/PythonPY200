from node import Node

from typing import Any, Optional, Iterable


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
