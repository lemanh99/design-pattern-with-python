from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass


class Dot(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f"Drawing dot at ({self.x}, {self.y})")


class CompoundGraphic(Graphic):
    def __init__(self):
        self.children: List[Graphic] = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        for child in self.children:
            child.draw()


class Circle(Dot):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print(f"Drawing circle at ({self.x}, {self.y}) with radius {self.radius}")


if __name__ == "__main__":
    compound_graphic = CompoundGraphic()
    compound_graphic.add(Dot(1, 2))
    compound_graphic.add(Dot(3, 4))
    compound_graphic.draw()

