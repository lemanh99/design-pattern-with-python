"""
Source: https://refactoring.guru/design-patterns/composite/python/example
"""
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    def __init__(self):
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component) -> None:
        pass

    def remove(self, component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def execute(self) -> str:
        pass


class Leaf(Component):
    def execute(self) -> str:
        return "Leaf"


class Composite(Component):
    def __init__(self):
        super().__init__()
        self._children: List[Component] = []

    def add(self, component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def execute(self) -> str:
        results = []
        for child in self._children:
            results.append(child.execute())
        return f"Branch({'+'.join(results)})"


class ClientCode:
    def __init__(self, component1: Component, component2: Component) -> None:
        self.component1 = component1
        self.component2 = component2

    def execute(self) -> None:
        if self.component1.is_composite():
            self.component1.add(self.component2)

        print(f"RESULT: {self.component1.execute()}")


if __name__ == "__main__":
    simple = Leaf()
    print("Client: I've got a simple component:")
    ClientCode(simple, None).execute()

    print("\n")

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    # print("Client: Now I've got a composite tree:")
    # ClientCode(tree, None).execute()

    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    ClientCode(branch1, simple).execute()
