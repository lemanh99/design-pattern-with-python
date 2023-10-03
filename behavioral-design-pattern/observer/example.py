from abc import ABC, abstractmethod


class EventListener(ABC):
    @abstractmethod
    def update(self, filename):
        pass


class EventManager:
    def __init__(self):
        self.listeners = []

    def subscribe(self, listener):
        self.listeners.append(listener)

    def unsubscribe(self, listener):
        self.listeners.remove(listener)

    def notify(self, filename):
        for listener in self.listeners:
            listener.update(filename)


class Editor:
    def __init__(self):
        self.event_manager = EventManager()

    def open_file(self, filename):
        self.event_manager.notify(filename)

    def save_file(self):
        pass


class EmailAlertsListener(EventListener):
    def __init__(self, email):
        self.email = email

    def update(self, filename):
        print(f'{self.email} received an alert: {filename}')


class LoggingListener(EventListener):
    def __init__(self, filename):
        self.filename = filename

    def update(self, filename):
        print(f'Logging to {self.filename}: {filename}')


if __name__ == '__main__':
    editor = Editor()
    editor.event_manager.subscribe(EmailAlertsListener('email@example.com'))
    editor.event_manager.subscribe(LoggingListener('log.txt'))
    editor.open_file('file.txt')
