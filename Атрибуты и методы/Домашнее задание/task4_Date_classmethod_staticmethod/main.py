class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = None
        self.month = None
        self.year = None

        self.is_valid_date(day, month, year)

    def is_leap_year(self):
        """Проверяет, является ли год високосным"""
        if self.year % 4 == 0:
            return True
        else:
            return False

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        self.month = month  # Присваиваем номеру месяца полученный от пользователя номер.
        self.year = year    # Присваимваем году полученный от пользователя год.
        list_of_days = 0    # По умолчанию берём количество дней из кортежа для невисокосных годов.

        if not 0 < self.month < 13:    # Проверяем корректность номера месяца
            raise ValueError('Такого месяца нет')

        if self.is_leap_year:   # Проверяем високосный, ли год
            list_of_days = 1    # Если да, переключаемся на кортеж с количеством дней для високосных.

        return self.DAY_OF_MONTH[list_of_days][self.month - 1]

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if year < 0:
            raise ValueError("Год может быть только нашей эры")
        self.year = year
        if not 0 < month < 13:
            raise ValueError('Такого месяца нет')
        self.month = month

        if self.is_leap_year:
            list_of_days = 1
        else:
            list_of_days = 0

        if day > self.DAY_OF_MONTH[list_of_days][self.month-1]:
            raise ValueError("В этом месяце нет столько дней")
        self.day = day

    def __str__(self):
        return f"{'{0:0>2}'.format(self.day)}/{'{0:0>2}'.format(self.month)}/{self.year}"

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"


if __name__ == "__main__":
    data = Date(25, 2, 1995)
    print(data.__dict__)
    foo = data.is_leap_year()
    print(foo)