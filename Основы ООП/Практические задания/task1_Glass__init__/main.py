from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Некорректный тип данных")
        if capacity_volume <= 0:
            raise ValueError("Недопустимое значение")
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Некорректный тип данных")
        if capacity_volume < occupied_volume or occupied_volume < 0:
            raise ValueError("Недопустимое значение, жидкости больше, чем вмещаемо")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume



if __name__ == "__main__":
    glass_1 = Glass(500, 100)
    glass_2 = Glass(100, 15)
    print(glass_1)
    print(glass_2)

    glass_3 = Glass(0, 500)
    glass_4 = Glass(500, 501)
    print(glass_3)

