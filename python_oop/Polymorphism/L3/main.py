class Rectangle:
    def overlaps(self, rect: "Rectangle") -> bool:
        s_left= self.get_left_x()
        s_right = self.get_right_x()
        s_bottom = self.get_bottom_y()
        s_top = self.get_top_y()

        r_left = rect.get_left_x()
        r_right = rect.get_right_x()
        r_bottom = rect.get_bottom_y()
        r_top = rect.get_top_y()

        if s_left > r_right or s_right < r_left:
            return False 
        if s_bottom > r_top or s_top < r_bottom:
            return False
        return True
    # don't touch below this line

    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self) -> int:
        return min(self.__x1, self.__x2)

    def get_right_x(self) -> int:
        return max(self.__x1, self.__x2)

    def get_top_y(self) -> int:
        return max(self.__y1, self.__y2)

    def get_bottom_y(self) -> int:
        return min(self.__y1, self.__y2)

    def __repr__(self) -> str:
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
