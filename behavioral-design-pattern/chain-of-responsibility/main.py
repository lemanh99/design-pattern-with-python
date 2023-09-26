"""
Source: https://refactoring.guru/design-patterns/chain-of-responsibility/python/example
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class BaseHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class ConcreteAHandlers(BaseHandler):

    def handle(self, request) -> Optional[str]:
        if request == "A":
            return f"ConcreteHandlerA: {request}"

        return super().handle(request)


class ConcreteBHandlers(BaseHandler):
    def handle(self, request) -> Optional[str]:
        if request == "B":
            return f"ConcreteHandlerB: {request}"

        return super().handle(request)


class ConcreteCHandlers(BaseHandler):
    def handle(self, request) -> Optional[str]:
        if request == "C":
            return f"ConcreteHandlerC: {request}"

        return super().handle(request)


class ClientCode:
    def __init__(self, handler: Handler):
        self.handler = handler

    def execute(self, request):
        result = self.handler.handle(request)
        if result:
            print(f"Result: {result}")
        else:
            print(f"Not found {request}")


if __name__ == "__main__":
    concrete_a = ConcreteAHandlers()
    concrete_b = ConcreteBHandlers()
    concrete_c = ConcreteCHandlers()
    concrete_a.set_next(concrete_b).set_next(concrete_c)
    client_code = ClientCode(concrete_a)
    client_code.execute("A")
    client_code.execute("B")
    client_code.execute("C")
