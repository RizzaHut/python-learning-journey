class Archer:
    name: str
    health: int
    num_arrows: int

    def __init__(self, name: str, health: int, num_arrows: int) -> None:
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def take_hit(self) -> None:
        self.health -= 1
        if self.health <= 0:
            raise Exception(f"{self.name} is dead")

    def shoot(self, target: "Archer") -> None:
        self.target = target
        if self.num_arrows <= 0:
            raise Exception(f"{self.name} can't shoot")
        self.num_arrows -= 1
        print(f"{self.name} shoots {self.target}")
        target.take_hit()

    # don't touch below this line

    def get_status(self) -> tuple[str, int, int]:
        return self.name, self.health, self.num_arrows

    def print_status(self) -> None:
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")
