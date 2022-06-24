import unittest

from main import Glass


class TestStr(unittest.TestCase):
    def test_str(self):
        """ Функция проверяет выполнение метода str """
        cap_vol = 500
        oc_vol = 300
        glass1 = Glass(cap_vol, oc_vol)
        expected_value = f"Стакан объёмом 500. Объём жидкости = 300"
        actual_value = str(glass1)
        self.assertEqual(expected_value, actual_value)