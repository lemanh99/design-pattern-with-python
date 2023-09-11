from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self):
        pass


class WindowButton(Button):
    def render(self):
        return "Window: Render button window done"

    def on_click(self):
        return "Window: Click button window done"


class HTMLButton(Button):
    def render(self):
        return "HTML: Render button html done"

    def on_click(self):
        return "HTML: Click html window done"


class Dialog(ABC):
    @abstractmethod
    def render(self):
        pass

    def create_button(self):
        button = self.render()
        result = f"Dialog: Create button \n {button.render()}"
        return result


class WindowDialog(Dialog):
    def render(self):
        return WindowButton()


class HTMLDialog(Dialog):
    def render(self):
        return HTMLButton()


class ClientCode:
    def __init__(self, dialog: Dialog):
        self.dialog = dialog

    def create_button(self):
        print(f"Client: Create button\n {self.dialog.create_button()}", end="")


if __name__ == "__main__":
    print("App: I am using window.")
    window_dialog = WindowDialog()
    client = ClientCode(window_dialog)
    client.create_button()
    print("\n")
    print("App: I am using WEB.")
    html_dialog = HTMLDialog()
    client = ClientCode(html_dialog)
    client.create_button()
