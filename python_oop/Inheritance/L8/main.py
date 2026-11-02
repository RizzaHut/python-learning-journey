class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
        min_x = min(x_1, x_2)
        max_x = max(x_1, x_2)
        min_y = min(y_1, y_2)
        max_y = max(y_1, y_2)

        return min_x <= self.pos_x <= max_x and min_y <= self.pos_y <= max_y
        


class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, fire_range: int) -> None:
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x: int, y: int, units: list[Unit]) -> list[Unit]:
        x_1 = x - self.__fire_range
        x_2 = x + self.__fire_range
        y_1 = y - self.__fire_range
        y_2 = y + self.__fire_range
        
        hit_by_blast = []

        for u in units:
            if u.in_area(x_1, y_1, x_2, y_2):
                hit_by_blast.append(u)

        return hit_by_blast
