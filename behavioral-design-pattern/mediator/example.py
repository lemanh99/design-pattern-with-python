from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event: str) -> None:
        pass


class Component:
    def __init__(self, dialog):
        self.dialog = dialog

    def click(self):
        print("Component click")

    def keypress(self):
        print("Component keypress")


class Button(Component):
    def click(self):
        print("Button click")
        self.dialog.notify(self, "click")

    def keypress(self):
        print("Button keypress")
        self.dialog.notify(self, "keypress")


class Textbox(Component):
    def click(self):
        print("Textbox click")
        self.dialog.notify(self, "click")

    def keypress(self):
        print("Textbox keypress")
        self.dialog.notify(self, "keypress")


class Checkbox(Component):
    def click(self):
        print("Checkbox click")
        self.dialog.notify(self, "click")

    def keypress(self):
        print("Checkbox keypress")
        self.dialog.notify(self, "keypress")

    def check(self):
        print("Checkbox check")
        self.dialog.notify(self, "check")


class AuthenticationDialog(Mediator):
    def __init__(self):
        self.title = None
        self.login_or_register = None
        self.login_username: Textbox = None
        self.login_password: Textbox = None
        self.register_username: Textbox = None
        self.register_password: Textbox = None
        self.register_email: Textbox = None
        self.oke: Button = None
        self.cancel: Button = None
        self.remember_me: Checkbox = None

    def notify(self, sender, event: str) -> None:
        if isinstance(sender, Textbox) and event == "check":
            sender.click()


if __name__ == "__main__":
    dialog = AuthenticationDialog()
    dialog.title = "Login or Register"
    dialog.login_or_register = "Login"
    dialog.login_username = Textbox(dialog)
    dialog.login_password = Textbox(dialog)
    dialog.register_username = Textbox(dialog)
    dialog.register_password = Textbox(dialog)
    dialog.register_email = Textbox(dialog)
    dialog.oke = Button(dialog)
    dialog.cancel = Button(dialog)
    dialog.notify(dialog.login_username, "check")
