from abc import ABC, abstractmethod


class StateInteface(ABC):
    @abstractmethod
    def click_lock(self):
        pass

    @abstractmethod
    def click_play(self):
        pass

    @abstractmethod
    def click_next(self):
        pass

    @abstractmethod
    def click_previous(self):
        pass


class State(StateInteface):
    def __init__(self, player=None):
        self._player = player

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    def click_lock(self):
        print('click_lock')

    def click_play(self):
        print('click_play')

    def click_next(self):
        print('click_next')

    def click_previous(self):
        print('click_previous')


class LockedState(State):
    def click_lock(self):
        print('LockedState')


class ReadyState(State):
    def click_play(self):
        print('ReadyState')


class PlayingState(State):
    def click_lock(self):
        print('PlayingState')


class Player:
    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: StateInteface):
        self._state = state
        self._state.player = self

    def click_lock(self):
        self._state.click_lock()

    def click_play(self):
        self._state.click_play()

    def click_next(self):
        self._state.click_next()

    def click_previous(self):
        self._state.click_previous()


if __name__ == '__main__':
    player = Player()
    player.state = LockedState()
    player.click_play()
    player.click_lock()
    player.click_next()
    player.click_previous()
    player.state = ReadyState()
    player.click_play()
    player.click_lock()
    player.click_next()
    player.click_previous()
    player.state = PlayingState()
    player.click_play()
    player.click_lock()
    player.click_next()
    player.click_previous()
