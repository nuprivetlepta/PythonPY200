from typing import Union

class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if not occupied_volume > 0:
            raise ValueError
        if occupied_volume > self.capacity_volume:
            raise ValueError
        self.occupied_volume = occupied_volume

    def init_add_water(self, added_water: Union[int, float]):
        if not isinstance(added_water, (int, float)):
            raise TypeError
        if not added_water > 0:
            raise ValueError
        self.occupied_volume += added_water

    def init_remove_water(self, removed_water: Union[int, float]):
        if not isinstance(removed_water, (int, float)):
            raise TypeError
        if not removed_water > 0:
            raise ValueError
        self.occupied_volume -= removed_water


if __name__ == '__main__':
    glass = Glass(500, 200)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.init_add_water(300)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.init_remove_water(200)
    print(glass.capacity_volume, glass.occupied_volume)
