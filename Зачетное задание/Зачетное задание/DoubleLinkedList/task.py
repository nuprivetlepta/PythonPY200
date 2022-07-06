from collections.abc import MutableSequence
from typing import Any, Iterable, Optional

from node import Node
from doublenode import DoubleLinkedNode


class LinkedList(MutableSequence):
    ANY_NODE = Node

    def __init__(self, data: Iterable = None):
        self._list_nodes = self.init_linked_list(data)  # fixme delete
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def init_linked_list(self, data: Iterable):  # fixme delete
        """ Метод, который создает вспомогательный список и связывает в нём узлы. """
        self._list_nodes = [self.ANY_NODE(value) for value in data]

        for i in range(len(self._list_nodes)-1):
            left_node = self._list_nodes[i]
            right_node = self._list_nodes[i+1]
            self.linked_nodes(left_node, right_node)
        return self._list_nodes

    @property
    def get_list_nodes(self):
        """Метод превращает python.list в неизменяемое свойство, это его геттер"""
        return self._list_nodes

    def step_by_step_on_nodes(self, index: int) -> ANY_NODE:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        # fixme delete unused
        # if not isinstance(index, int):
        #     raise TypeError("Индекс может быть только целочисленным")
        #
        # if not 0 <= index < self._len:  # для for
        #     raise IndexError()
        self.index_test(index)

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node

        # iter_nodes = iter(self)
        # for _ in range(index):
        #     current_node = next(iter_nodes)
        # return current_node

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = self.ANY_NODE(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    @staticmethod
    def linked_nodes(left_node: ANY_NODE, right_node: Optional[ANY_NODE] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index):  # todo return node or node.value
        """ Метод возвращает значение узла по указанному индексу. """
        _node = self.step_by_step_on_nodes(index)
        return _node

    # def __setitem__(self, key, value): "Почему автоматически появляются key, value?"
    #     pass

    def __setitem__(self, index: int, value: Any):
        """Метод присваивает введенное значение узлу"""
        _node = self.step_by_step_on_nodes(index)
        _node.value = value

    def __delitem__(self, index: int):
        """Метод удаляет ноду из нашего списка и связывает соседние"""
        # if not isinstance(index, int):  # Проверяем валидность индекса по типу.
        #     raise TypeError
        #
        # if not 0 <= index < self._len:   # Проверяем валидность индекса по диапазону значения.
        #     raise IndexError ЗАМЕНЕНО МЕТОДОМ index_test
        self.index_test(index)

        del_node = self.step_by_step_on_nodes(index)    # Находим ноду ранее написанным итератором

        if del_node is self._head:   # Проверка удаляемой ноды, а ни первая ли она?
            self.head = del_node.next   # fixme check self.head Присваемваем голове списка "вторую" ноду.
        elif index == self._len - 1:    # Проверка удаляемой ноды, ни последняя ли она?
            prev_node = self.step_by_step_on_nodes(index - 1)   # Объявляем предыдущую ноду
            self.linked_nodes(prev_node, None)    # Очищаем у ставшей последней ноды ссылку next
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)   # Ищем предыдущую
            next_node = self.step_by_step_on_nodes(index + 1)   # Ищем следующую
            self.linked_nodes(prev_node, next_node)     # Связываем граничные ноды
        self._len -= 1    # После каждого выполнения метода убираем одну единицу из длины.

    def __len__(self):
        """Метод превращает наш атрибут self.len в свойство, это геттер,
        сеттер не нужен, т.к. пользователь не меняет значение длины напрямую,
        все её изменения вытекают из методов удаления/добавления элементов"""
        return self._len

    def insert(self, index: int, value: Any) -> None:
        """
        :param index: Место в списке, на котором будет стоять нода со значением
        :param value: Значение, хранящееся в добавляемой ноде
        :return: Метод ничего не возвращает, выполняет добавление в существующий список
        """
        if not isinstance(index, int):  # Проверяем тип индекса
            raise TypeError
        insert_node = self.ANY_NODE(value)  # Создаём экземпляр класса с переданным значением

        if 0 < index < self._len:  # Проверка индекса без помощи index_test т.к. IndexError сломает суть метода.
            prev_node = self.step_by_step_on_nodes(index - 1)  # Находим предыдущую ноду
            current_node = self.step_by_step_on_nodes(index)  # Находим подвигаемую ноду.
            self.linked_nodes(insert_node, current_node)  # Связываем нашу ноду с подвигаемой
            self.linked_nodes(prev_node, insert_node)  # Связываем предыдущую ноду с вставленной.

        elif index == 0:
            current_node = self._head  # Заводим переменную с "головой" списка
            self.linked_nodes(insert_node, current_node)  # Связываем вставляемую ноду с подвигаемой
            self._head = insert_node  # Переназначаем "голову" списка

        elif index >= self._len:  # Проверка индекса, вне рамок нашего списка.
            prev_node = self.step_by_step_on_nodes(self._len - 1)  # Находим последнюю ноду
            self.linked_nodes(prev_node, insert_node)  # Вставляем нашу ноду в конец списка
        self._len += 1  # Увеличиваем длину списка после добавления.

    """Блок доп. заданий"""
    def index_test(self, index):    # Метод может быть статическим, если убрать из него проверку IndexError
        """проверка передаваемого индекса на валидность"""
        if not isinstance(index, int):
            raise TypeError("Может быть только целочисленным")
        if not 0 <= index < self._len:
            raise IndexError("Недопустимое значение (меньше 0 или больше длины)")

    def index(self, value: Any, start=0, stop=None) -> int:
        searched_value = value

        self.index_test(start)

        if stop is not None:
            self.index_test(stop)
        else:
            stop = self._len  # len(self)
        for i in range(start, stop):
            node_ = self.step_by_step_on_nodes(i)
            if node_.value == searched_value:
                return i

        raise ValueError("Нода с таким значением не найдена")

    def __iter__(self):
        """Наш итератор"""
        return self.iter_gen()

    def iter_gen(self):
        """генератор для итератора"""
        current_node = self._head
        for _ in range(self._len):
            yield current_node
            current_node = current_node.next

    def __contains__(self, value):
        """"Поиск содержимого. Пока что возвращает true только со значением 1 :( """
        search = value
        for node_ in self.iter_gen():
            if str(node_.value) == search:
                return True

        return False

    def count(self, value: Any) -> int:
        search = value
        count = 0
        for node_ in self.iter_gen():
            if node_.value == search:  # str не нужен
                count += 1
        return count  # один раз в конце

    def pop(self, index: int = ...) -> Any:
        popped = self.step_by_step_on_nodes(index)
        self.linked_nodes(self.step_by_step_on_nodes(index - 1), popped.next)
        return f"popped value is {popped.value}"  # fixme popped.value

    def extend(self, values: Iterable[Any]) -> None:
        for value in values:
            self.append(value)

    def remove(self, value: Any) -> None:
        del_key = value
        for index, node_ in enumerate(self.iter_gen()):
            if str(node_.value) == str(del_key):  # fixme delete str
                self.__delitem__(index)  # fixme del self[index]

    def __repr__(self):
        # todo return f"{self.__class__.__name__}({[node.value for node in self]})"
        return f"{self.__class__.__name__}({self._list_nodes})"

    def __str__(self):
        # todo return f"{self.__class__.__name__}({[node.value for node in self]})"
        return f"{self._list_nodes}"


class DoubleLinkedList(LinkedList):
    ANY_NODE = DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        right_node.prev = left_node


if __name__ == '__main__':
    list_ = ["foo", "bar", 3, 4, "55"]
    dll = DoubleLinkedList(list_)
    print(repr(dll))
    print('...')
    print(dll)
    dll.__delitem__(0)

    print(f"Zero index: {dll[0]}")
    print(f'golova {dll.head}')
    print(dll)
    print('...')
    print('...')
    print('...')
    print(f"Get list nodes {dll.get_list_nodes}")

    node_0 = DoubleLinkedNode('prev')
    node_1 = DoubleLinkedNode(1)
    node_2 = DoubleLinkedNode(2)
    DoubleLinkedList.linked_nodes(node_1, node_2)
    DoubleLinkedList.linked_nodes(node_0, node_1)
    print(repr(node_1))
    print(node_1)

    # print(f"index foo{dll.index('foo')}")
    # print(dll.index("bar"))
    print(dll.index("55"))
