class Wall:
    armor: int = 10
    height: int = 5

    def get_cost(self) -> int:
        cost = self.armor * self.height
        return cost

    # don't touch below this line

    def fortify(self) -> None:
        self.armor *= 2
