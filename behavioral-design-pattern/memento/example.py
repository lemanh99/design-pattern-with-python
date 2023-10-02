class Editor:
    def __init__(self):
        self._text = ""
        self._cursor_x = 0
        self._cursor_y = 0
        self._selection_width = 0

    def set_text(self, text):
        self._text = text

    def set_cursor(self, x, y):
        self._cursor_x = x
        self._cursor_y = y

    def set_selection_width(self, width):
        self._selection_width = width

    def create_snapshot(self):
        return Snapshot(
            self,
            self._text,
            self._cursor_x,
            self._cursor_y,
            self._selection_width
        )


class Snapshot:
    def __init__(self, editor, text, cursor_x, cursor_y, selection_width):
        self._editor = editor
        self._text = text
        self._cursor_x = cursor_x
        self._cursor_y = cursor_y
        self._selection_width = selection_width

    def restore(self):
        self._editor.set_text(self._text)
        self._editor.set_cursor(self._cursor_x, self._cursor_y)
        self._editor.set_selection_width(self._selection_width)

    def create_snapshot(self):
        self._editor.create_snapshot()


class Command:
    def __init__(self):
        self._backup = None

    def make_backup(self, snapshot):
        self._backup = snapshot.create_snapshot()

    def undo(self):
        self._backup.restore()


if __name__ == '__main__':
    editor = Editor()
    editor.set_text("Hello world")
    editor.set_cursor(2, 3)
    editor.set_selection_width(5)
    snapshot = Snapshot(editor, "snapshot", 1, 1, 1)
    command = Command()
    command.make_backup(snapshot)
