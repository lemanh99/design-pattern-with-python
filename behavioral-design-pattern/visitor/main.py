from abc import ABC, abstractmethod
from typing import List


class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def feature_a(self):
        return "Feature A"


class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def feature_b(self):
        return "Feature B"


class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass


class ConcreteVisitors(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{element.feature_a()} + ConcreteVisitor1")

    def visit_concrete_element_b(self, element):
        print(f"{element.feature_b()} + ConcreteVisitor1")


class ClientCode:
    def __init__(self, elements: List[Element], visitor: Visitor):
        self._elements = elements
        self._visitor = visitor

    def execute(self):
        for element in self._elements:
            element.accept(self._visitor)


if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]
    visitor = ConcreteVisitors()
    client = ClientCode(elements, visitor)
    client.execute()
