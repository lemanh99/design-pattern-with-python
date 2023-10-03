from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def do_this(self) -> None:
        pass

    @abstractmethod
    def do_that(self) -> None:
        pass


class ConcreteStates(State):
    def __init__(self):
        self._context = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    def do_this(self) -> None:
        print('do this')

    def do_that(self) -> None:
        print('do that')


class Context:
    def __init__(self, state: State) -> None:
        self._state = state
        self._state.context = self

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: State) -> None:
        self._state = state
        self._state.context = self

    def do_this(self) -> None:
        self._state.do_this()

    def do_that(self) -> None:
        self._state.do_that()


if __name__ == '__main__':
    context = Context(ConcreteStates())
    context.do_this()
    context.do_that()
    context.state = ConcreteStates()
    context.do_this()
    context.do_that()
