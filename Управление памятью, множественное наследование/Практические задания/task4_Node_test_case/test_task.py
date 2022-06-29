import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        node = Node(1)
        self.assertIsNone(node.next, msg="При иницализации следующий узел не None")
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""

        second_node = Node("second_node")
        first_node = Node("first_node", next_=second_node)
        break_node = Node("second_node")

        expected_object = second_node
        actual_object = first_node.next
        self.assertIs(expected_object, actual_object,
                      msg="Узлы не эквиваленты")

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node_value = 5
        node = Node(node_value)
        expected_value = f"Node({node_value}, None)"
        actual_value = repr(node)
        self.assertEqual(expected_value, actual_value,
                         msg="Неверный repr для ноды без след. узла")

    @unittest.skip(reason="Ещё не реализованная функциональность")
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)
        expected_value = str(some_value)

        self.assertEqual(expected_value, str(node))
        self.assertEqual(expected_value, f"{node}")
        # TODO проверить строковое представление

    def test_is_valid(self):
        Node.is_valid(Node(5))
        Node.is_valid(None)

        with self.assertRaises(TypeError):
            invalid_node = "invalid_node"
            Node.is_valid(invalid_node)

        # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
