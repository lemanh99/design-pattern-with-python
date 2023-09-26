from abc import abstractmethod


class Command:
    def __init__(self, app, editor):
        self._app = app
        self._editor = editor
        self._backup = None

    def save_backup(self):
        self._backup = self._editor.text

    def undo(self):
        self._editor.text = self._backup

    @abstractmethod
    def execute(self):
        pass


class CopyCommand(Command):
    def execute(self):
        self._app.clipboard = self._editor.get_selection()


class CutCommand(Command):
    def execute(self):
        self.save_backup()
        self._app.clipboard = self._editor.get_selection()
        self._editor.delete_selection()


class PasteCommand(Command):
    def execute(self):
        self.save_backup()
        self._editor.replace_selection(self._app.clipboard)


class UndoCommand(Command):
    def execute(self):
        self.undo()


class Editor:
    def __init__(self):
        self.test = None

    def get_selection(self):
        return self.test

    def delete_selection(self):
        self.test = ""

    def replace_selection(self, text):
        self.test = text


class CommandHistory:
    def __init__(self):
        self._history = []

    def push(self, command):
        self._history.append(command)

    def pop(self):
        return self._history.pop()

    def is_empty(self):
        return len(self._history) == 0


class Application:
    def __init__(self):
        self.clipboard = None
        self.editors = []
        self.active_editor = None
        self.history = CommandHistory()

    def create_ui(self):
        self.editors.append(Editor())
        self.active_editor = self.editors[0]
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.push(command)

    def undo(self):
        if not self.history.is_empty():
            self.history.pop().undo()
