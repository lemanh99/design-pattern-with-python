from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class WinButton(Button):
    def render(self):
        print("WinButton: Render a button in a Windows style.")


class MacButton(Button):
    def render(self):
        print("MacButton: Render a button in a Mac style.")


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


class WinCheckbox(Checkbox):
    def render(self):
        print("WinCheckbox: Render a checkbox in a Windows style.")


class MacCheckbox(Checkbox):
    def render(self):
        print("MacCheckbox: Render a checkbox in a Mac style.")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Application(ABC):
    def __init__(self, factory: GUIFactory):
        self._factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self._factory.create_button()
        self.checkbox = self._factory.create_checkbox()

    def paint(self):
        self.button.render()
        self.checkbox.render()


if __name__ == "__main__":
    print("Configuring Windows application...")
    application = Application(WinFactory())
    application.create_ui()
    application.paint()

    print("Configuring Mac application...")
    application = Application(MacFactory())
    application.create_ui()
    application.paint()
