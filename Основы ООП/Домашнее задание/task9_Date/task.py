class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = None
        self.init_day(day)
        self.month = None
        self.init_month(month)
        self.year = None
        self.init_year(year)

    def init_day(self, day: int):
        if not isinstance(day, int):
            raise TypeError
        self.day = day

    def init_month(self, month: int):
        if not isinstance(month, int):
            raise TypeError
        self.month = month

    def init_year(self, year: int):
        if not isinstance(year, int):
            raise TypeError
        self.year = year

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.day}, {self.month}, {self.year})"

    def __str__(self) -> str:
        return f"{'{0:0>2}'.format(self.day)}/{'{0:0>2}'.format(self.month)}/{self.year}"


if __name__ == '__main__':
    date = Date(22, 6, 1995)
    print(date)
    print(repr(date))
