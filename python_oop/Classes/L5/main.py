class Wall:
    def __init__(self, depth: int, height: int, width: int) -> None:
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = depth * height * width

