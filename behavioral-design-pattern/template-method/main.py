from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.step1()
        self.step2()
        self.step3()
        self.step4()

    def step1(self) -> None:
        print("AbstractClass.step1")

    def step2(self) -> None:
        print("AbstractClass.step2")

    @abstractmethod
    def step3(self) -> None:
        pass

    @abstractmethod
    def step4(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    def step3(self) -> None:
        print("ConcreteClass1.step3")

    def step4(self) -> None:
        print("ConcreteClass1.step4")


class ConcreteClass2(AbstractClass):
    def step1(self) -> None:
        print("ConcreteClass2.step1")

    def step2(self) -> None:
        print("ConcreteClass2.step2")

    def step3(self) -> None:
        print("ConcreteClass2.step3")

    def step4(self) -> None:
        print("ConcreteClass2.step4")

class ClientCode:
    def __init__(self, abstract_class):
        self.abstract_class = abstract_class

    def execute(self):
        self.abstract_class.template_method()


if __name__ == "__main__":
    concrete_class1 = ConcreteClass1()
    concrete_class2 = ConcreteClass2()

    client_code1 = ClientCode(concrete_class1)
    client_code1.execute()

