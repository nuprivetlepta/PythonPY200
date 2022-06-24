from main import Glass

import unittest


class TestCase(unittest.TestCase):
    def test_base_initiation(self):
        full_vol = 1000
        occupied_vol = 500
        glass = Glass(full_vol, occupied_vol)
        expected_value = f"1000 500"
        actual_value = f"{glass.capacity_volume} {glass.occupied_volume}"
        # assert expected_value == actual_value
        self.assertEqual(str(expected_value), str(actual_value))

    @unittest.expectedFailure  # Декоратор, превращающий функцию в "детектор ошибок"
    def test_failure(self):
        """Функция проверяет появление ошибки при отрицательном значении объема"""
        full_vol = -111  # задаём отрицательное значение, вызывающее ошибку.
        oc_vol = 5  # задаём объем добавленной воды в соответствии с условием.
        glass1 = Glass(full_vol, oc_vol)  # Инициируем объект класса "Стакан"
        expected_value = f"-111 5"  # Ожидаемое значение
        actual_value = f"{glass1.capacity_volume} {glass1.occupied_volume}"  # Значение на выходе
        self.assertEqual(str(expected_value), str(actual_value))  # Сравнение значений.
