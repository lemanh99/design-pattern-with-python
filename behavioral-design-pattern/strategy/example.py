from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b


class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute(self, a, b):
        return self._strategy.execute(a, b)


if __name__ == "__main__":
    context = Context(ConcreteStrategyAdd())
    print(context.execute(1, 2))
    context.strategy = ConcreteStrategySubtract()
    print(context.execute(1, 2))
