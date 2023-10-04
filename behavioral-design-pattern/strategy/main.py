from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute(self, data):
        return self._strategy.execute(data)


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        print("Strategy A", data)


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        print("Strategy B", data)


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    context.execute("data")
    context.strategy = ConcreteStrategyB()
    context.execute("data")
