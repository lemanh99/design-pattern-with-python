from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_step_a(self):
        pass

    @abstractmethod
    def build_step_b(self):
        pass

    @abstractmethod
    def build_step_z(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self._product = None
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def build_step_a(self):
        self._product.add("ConcreteBuilder1: Step A")

    def build_step_b(self):
        self._product.add("ConcreteBuilder1: Step B")

    def build_step_z(self):
        self._product.add("ConcreteBuilder1: Step Z")


class ConcreteBuilder2(Builder):
    def __init__(self):
        self._product = None
        self.reset()

    def reset(self):
        self._product = Product2()

    def build_step_a(self):
        self._product.add("ConcreteBuilder2: Step A")

    def build_step_b(self):
        self._product.add("ConcreteBuilder2: Step B")

    def build_step_z(self):
        self._product.add("ConcreteBuilder2: Step Z")


class Product1:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Product2:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def change_builder(self, builder: Builder):
        self._builder = builder

    def build_minimal_viable_product(self):
        self._builder.build_step_a()

    def build_full_featured_product(self):
        self._builder.build_step_a()
        self._builder.build_step_b()
        self._builder.build_step_z()

    def make(self, type_builder: str):
        _build_handler = {
            'simple': self.build_minimal_viable_product,
            'full': self.build_full_featured_product
        }
        _build_handler.get(type_builder)()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.make('simple')
    builder.product.list_parts()
    print("\n")
    print("Standard full featured product: ")
    director.make('full')
    builder.product.list_parts()
