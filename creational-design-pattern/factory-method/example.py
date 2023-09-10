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


def client_code(dialog: Dialog) -> None:
    print(f"Client: Create button\n {dialog.create_button()}", end="")


if __name__ == "__main__":
    print("App: I am using window.")
    client_code(WindowDialog())
    print("\n")

    print("App: I am using WEB.")
    client_code(HTMLDialog())
