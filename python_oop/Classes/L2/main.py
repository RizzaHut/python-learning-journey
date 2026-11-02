class Wall:
    armor: int = 10
    height: int = 5

    def fortify(self) -> None:
        self.armor *= 2
