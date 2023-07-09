from editor.core import *
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import numpy as np


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)


class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.lineNumberArea = LineNumberArea(self)
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.updateLineNumberAreaWidth(0)

        # Set font size for text editor
        font = QFont()
        font.setPointSize(12)  # Increase the font size as desired
        self.setFont(font)

    def lineNumberAreaWidth(self):
        digits = 1
        max_value = max(1, self.blockCount())
        while max_value >= 10:
            max_value /= 10
            digits += 1
        space = 32 + digits  # self.fontMetrics().width('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), self.palette().color(QPalette.Window))

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = round(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + round(self.blockBoundingRect(block).height())

        current_line_number = self.textCursor().blockNumber() + 1

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(Qt.black)
                if block_number + 1 == current_line_number:
                    painter.setPen(Qt.red)  # Set the pen color to red for the current line number
                painter.drawText(0, top, self.lineNumberArea.width(), self.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            block_number += 1

    def highlightCurrentLine(self):
        """
        extra_selections = []

        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            line_color = QColor(Qt.yellow).lighter(160)
            selection.format.setBackground(line_color)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extra_selections.append(selection)

        self.setExtraSelections(extra_selections)
        """


class TextProvider(Module):
    text_editor: CodeEditor

    # Runs a script in cmd. Makes sure to keep cmd open until the user presses enter after script execution is completed.
    def run_script(self, text_editor: CodeEditor):
        pass

    def toggle_copilot(self, window: MainWindow):
        copilot_button = window.findChild(QPushButton, "copilot_button")
        if copilot_button.text() == "Copilot: Enabled":
            copilot_button.setText("Copilot: Disabled")
            copilot_button.setStyleSheet("background-color: red")
        else:
            copilot_button.setText("Copilot: Enabled")
            copilot_button.setStyleSheet("background-color: green")

    def open_file_dialogue(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            file = open(file_name, "r")
            with file:
                text = file.read()
                self.text_editor.setPlainText(text)

    def save_text_editor_content(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]
            text_content = self.text_editor.toPlainText()
            with open(file_name, "w") as file:
                file.write(text_content)

    def open_provider_window(self, window: MainWindow):
        self.text_editor = CodeEditor()
        window.set_inner_widget(self.text_editor)

        # Add a green run script button to the right dockbar
        run_script_button = QPushButton("\U0001F4DC Run Script")
        run_script_button.setStyleSheet("background-color: green")
        run_script_button.clicked.connect(lambda: self.run_script(self.text_editor))
        window.right_sidebar.widgets.addWidget(run_script_button)

        # Add other action buttons as well
        new_file_button = QPushButton("\U0001F4C4 New File")
        open_file_button = QPushButton("\U0001F4C2 Open File")
        new_file_button.clicked.connect(self.open_file_dialogue)
        open_file_button.clicked.connect(self.open_file_dialogue)
        hbox = QHBoxLayout()
        hbox.addWidget(new_file_button)
        hbox.addWidget(open_file_button)
        window.right_sidebar.widgets.addLayout(hbox)

        save_file_button = QPushButton("\U0001F4BE Save")
        save_file_button.setStyleSheet("background-color: blue")
        save_file_button.clicked.connect(self.save_text_editor_content)
        window.right_sidebar.widgets.addWidget(save_file_button)

        # Add a text editor copilot button at the statusbar
        copilot_button = QPushButton("Copilot: Enabled", window)
        copilot_button.setObjectName("copilot_button")
        copilot_button.setStyleSheet("background-color: green")
        copilot_button.clicked.connect(lambda: self.toggle_copilot(window))
        window.status_bar.addPermanentWidget(copilot_button)



    def create_toolbar_entry(self, window: MainWindow):
        action = window.toolbar.addAction("\U0001F4C4 Text Editor")
        action.triggered.connect(lambda: self.open_provider_window(window))

    def on_window(self, window: MainWindow):
        self.create_toolbar_entry(window)


text_provider = TextProvider("text_provider")
print("text_provider loaded")
