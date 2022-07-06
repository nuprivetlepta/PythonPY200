# fixme Проверить после удаления первого узла в двусвязном списке чему равен prev у head

from task import LinkedList, DoubleLinkedList, Node, DoubleLinkedNode

import unittest


class TestCase(unittest.TestCase):

    def test_head_reload_ll(self):
        list_ = [1, 2, 3, 4]
        ll = LinkedList(list_)
        ll.__delitem__(0)
        expected_value = f"[Node(2, 3), Node(3, 4), Node(4, None)]"
        actual_value = ll.__str__()

        self.assertEqual(str(expected_value), str(actual_value))


class TestCaseDll(unittest.TestCase):

    def test_head_reload_dll(self):
        list_ = [1, 2, 3, 4]
        dll = DoubleLinkedList(list_)
        dll.__delitem__(0)
        expected_value = f"[(None, 2, 3), (2, 3, 4), (3, 4, None)]"
        actual_value = dll.__str__()

        self.assertEqual(str(expected_value), str(actual_value))
        self.assertIsNone(dll._head.prev)


class TestCaseDllMiddle(unittest.TestCase):

    def test_head_reload_dll(self):
        list_ = [1, 2, 3, 4]
        dll = DoubleLinkedList(list_)
        dll.__delitem__(1)
        expected_value = f"[(None, 1, 3), (1, 3, 4), (3, 4, None)]"
        actual_value = dll.__str__()

        self.assertEqual(str(expected_value), str(actual_value))