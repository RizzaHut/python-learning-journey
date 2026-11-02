class Wizard:
    def __init__(self, name: str, stamina: int, intelligence: int) -> None:
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = stamina * 100
        self.mana = intelligence * 10
        
