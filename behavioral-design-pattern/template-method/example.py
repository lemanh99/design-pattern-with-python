from abc import ABC, abstractmethod


class GameAI(ABC):
    def __init__(self, name):
        self.name = name

    def play(self):
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    def collect_resources(self):
        print(f"{self.name} collects resources")

    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def build_units(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class OrcsAI(GameAI):
    def build_structures(self):
        print(f"{self.name} builds structures")

    def build_units(self):
        print(f"{self.name} builds units")

    def attack(self):
        print(f"{self.name} attacks")


class MonstersAI(GameAI):
    def build_structures(self):
        print(f"{self.name} builds structures")

    def build_units(self):
        print(f"{self.name} builds units")

    def attack(self):
        print(f"{self.name} attacks")


if __name__ == "__main__":
    orcs_ai = OrcsAI("Orcs")
    orcs_ai.play()

    monsters_ai = MonstersAI("Monsters")
    monsters_ai.play()
