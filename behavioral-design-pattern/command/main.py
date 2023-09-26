from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand1(Command):
    def __init__(self, receiver, params: str):
        self._receiver = receiver
        self._params = params

    def execute(self):
        self._receiver.excute(self._params)


class ConcreteCommand2(Command):

    def execute(self):
        print("ConcreteCommand2: execute")


class Receiver:
    def excute(self, params: str):
        print(f"Receiver: execute {params}")


class Invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

        self._commands.clear()


class ClientCode:
    def __init__(self):
        self._invoker = Invoker()
        self._receiver = Receiver()

    def do_something(self):
        self._invoker.add_command(ConcreteCommand1(self._receiver, "param1"))
        self._invoker.add_command(ConcreteCommand2())
        self._invoker.execute_commands()


if __name__ == "__main__":
    client = ClientCode()
    client.do_something()
