class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

        if not isinstance((self.day, self.month, self.year), int):
            raise TypeError("Значения должны быть  int")

    def __repr__(self):
        ...

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


date = Date(12, 12, 12)
print(date)

# TODO class Date