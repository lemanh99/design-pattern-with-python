from abc import ABC, abstractmethod


class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self):
        pass


class Component(ComponentWithContextualHelp):

    def __init__(self, container):
        self._container = container
        self.tooltip_text = None

    def show_help(self):
        if self.tooltip_text:
            print(f"showing tooltip: {self.tooltip_text}")
        else:
            self._container.show_help()


class Container(Component):

    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)
        child._container = self


class Button(Component):

    def __init__(self, container):
        super().__init__(container)
        self.tooltip_text = "Button tooltip"

    def click(self):
        self.show_help()


class Panel(Container):

    def __init__(self, modal_help_text):
        super().__init__()
        self.modal_help_text = modal_help_text

    def show_help(self):
        if self.modal_help_text:
            print(f"showing modal help: {self.modal_help_text}")
        else:
            super().show_help()


class Dialog(Container):
    def __init__(self, wiki_page_url):
        super().__init__()
        self.wiki_page_url = wiki_page_url

    def show_help(self):
        if self.wiki_page_url:
            print(f"opening wiki page: {self.wiki_page_url}")
        else:
            super().show_help()


class Application:
    def __init__(self):
        self.dialog = Dialog("https://www.google.com")
        self.panel = Panel("Panel help text")
        self.button = Button(self.panel)
        self.panel.add(self.button)
        self.dialog.add(self.panel)

    def click_button(self):
        self.button.click()

    def show_help(self):
        self.dialog.show_help()

if __name__ == "__main__":
    app = Application()
    app.click_button()
    app.show_help()
