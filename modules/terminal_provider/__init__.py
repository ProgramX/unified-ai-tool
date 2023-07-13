
from editor.core import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class TerminalWidget(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the background and foreground colors
        self.setStyleSheet("background-color: black; color: white;")

        # Set the console font
        font = QFont("Courier New")
        self.setFont(font)

        # Set the block cursor
        cursor = QTextCursor(self.document())
        cursor.insertBlock()
        cursor.insertText(' ')  # Insert a space as a placeholder
        cursor.movePosition(QTextCursor.PreviousCharacter)
        self.setTextCursor(cursor)

        # Disable line wrapping
        self.setLineWrapMode(QPlainTextEdit.NoWrap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.handle_return_pressed()
        else:
            super().keyPressEvent(event)

    def handle_return_pressed(self):
        # Get the user input
        user_input = self.toPlainText().split('\n')[-1]

        # Add the output to the terminal display
        output = f"You wrote: {user_input}\n"
        self.appendPlainText(output)

        # Move the cursor to the new line
        self.moveCursor(QTextCursor.End)

        # Clear the input line
        self.clearInputLine()

    def clearInputLine(self):
        # Clear the current input line
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.StartOfLine)
        cursor.movePosition(QTextCursor.EndOfLine, QTextCursor.KeepAnchor)
        cursor.removeSelectedText()
        self.setTextCursor(cursor)


class TerminalProvider(Module):

    def on_ready(self, window: MainWindow):
        window.bottom_bar.setWidget(TerminalWidget())


terminal_provider = TerminalProvider("terminal_provider")
print("terminal_provider loaded")