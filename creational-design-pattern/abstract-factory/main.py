from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def useful_func_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_func_a(self) -> str:
        return "ConcreteProductA1: The result of the product A1."


class ConcreteProductA2(AbstractProductA):

    def useful_func_a(self) -> str:
        return "ConcreteProductA2: The result of the product A2."


class AbstractProductB(ABC):
    @abstractmethod
    def useful_func_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_func_b(self, collaborator: AbstractProductA) -> None:
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_func_b(self) -> str:
        return "ConcreteProductB1: The result of the product B1."

    def another_useful_func_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_func_a()
        return f"The result of the B1 collaborating with: ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_func_b(self) -> str:
        return "ConcreteProductB2: The result of the product B2."

    def another_useful_func_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_func_a()
        return f"The result of the B2 collaborating with: ({result})"


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class ClientCode:
    def __init__(self, factory: AbstractFactory) -> None:
        self._factory = factory

    def some_operation(self) -> None:
        product_a = self._factory.create_product_a()
        product_b = self._factory.create_product_b()

        print(f"{product_b.useful_func_b()}")
        print(f"{product_b.another_useful_func_b(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    ClientCode(ConcreteFactory1()).some_operation()
    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    ClientCode(ConcreteFactory2()).some_operation()
