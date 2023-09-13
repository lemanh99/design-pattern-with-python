# Source: https://refactoring.guru/design-patterns/factory-method/python/example
from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProductA(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProductB(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreatorA(Creator):

    def factory_method(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works. \n {creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreatorA())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreatorB())
