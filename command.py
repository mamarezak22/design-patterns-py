from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class TextEditor:
    def __init__(self):
        self.content = ""

    def type_text(self, text):
        self.content += text

    def clear(self):
        self.content = ""

    def __str__(self):
        return self.content


class TypeCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.type_text(self.text)

    def undo(self):
        self.editor.content = self.editor.content[:-len(self.text)]


class ClearCommand(Command):
    def __init__(self, editor):
        self.editor = editor
        self.prev_content = ""

    def execute(self):
        self.prev_content = self.editor.content
        self.editor.clear()

    def undo(self):
        self.editor.content = self.prev_content


class EditorInvoker:
    def __init__(self):
        self.history = []

    def run(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            self.history.pop().undo()

def main():
    editor = TextEditor()
    invoker = EditorInvoker()

    invoker.run(TypeCommand(editor, "Hello "))
    invoker.run(TypeCommand(editor, "World!"))
    print(editor)  

    invoker.undo()
    print(editor) 

    invoker.run(ClearCommand(editor))
    print(editor)

    invoker.undo()
    print(editor)

main()