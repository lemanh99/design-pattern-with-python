from abc import ABC, abstractmethod
from typing import List


class Subscriber(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class ConcreteSubscribers(Subscriber):
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print(f'{self.name} received message: {message}')


class Publisher:
    def __init__(self) -> None:
        self.subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber) -> None:
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        self.subscribers.remove(subscriber)

    def notify(self, message: str) -> None:
        for subscriber in self.subscribers:
            subscriber.update(message)

    def main_business_logic(self) -> None:
        self.notify('Important message!')


if __name__ == '__main__':
    publisher = Publisher()
    subscriber_1 = ConcreteSubscribers('Subscriber 1')
    publisher.subscribe(subscriber_1)
    publisher.subscribe(ConcreteSubscribers('Subscriber 2'))
    publisher.subscribe(ConcreteSubscribers('Subscriber 3'))
    publisher.main_business_logic()
    publisher.unsubscribe(subscriber_1)
    publisher.main_business_logic()
