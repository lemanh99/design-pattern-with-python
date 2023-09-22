"""
Source: https://refactoring.guru/design-patterns/bridge/python/example
"""
from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return f"Abstraction: Base operation with:\n" \
               f"{self.implementation.operation_implementation()}"


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return f"ExtendedAbstraction: Extended operation with:\n" \
               f"{self.implementation.operation_implementation()}"


class ClientCode:
    def __init__(self, abstraction: Abstraction) -> None:
        self.abstraction = abstraction

    def operation(self) -> None:
        print(self.abstraction.operation())


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client = ClientCode(abstraction)
    client.operation()

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client = ClientCode(abstraction)
    client.operation()
