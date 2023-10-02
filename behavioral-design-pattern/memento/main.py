from abc import ABC, abstractmethod


class Memento(ABC):
    @abstractmethod
    def restore(self):
        pass


class Originator(ABC):
    @abstractmethod
    def save(self):
        pass


class ConcreteMemento:
    def __init__(self, originator, state):
        self._originator = originator
        self._state = state

    def restore(self):
        return self._state

    def get_state(self):
        return self._state


class ConcreteOriginator(Originator):
    def __init__(self, state):
        self._state = state

    def save(self):
        return ConcreteMemento(self, self._state)

    def restore(self, memento):
        self._state = memento.restore()

    def get_state(self):
        return self._state


class CareTaker:
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def backup(self):
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        self._originator.restore(memento)

    def show_history(self):
        for memento in self._mementos:
            print(memento.get_state())


if __name__ == '__main__':
    originator = ConcreteOriginator('A')
    care_taker = CareTaker(originator)
    care_taker.backup()
    originator.get_state()
    originator._state = 'B'
    care_taker.backup()
    originator.get_state()
    originator._state = 'C'
    care_taker.backup()

    care_taker.show_history()
