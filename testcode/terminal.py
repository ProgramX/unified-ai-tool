import sys
from PySide6.QtCore import Qt, QProcess
from PySide6.QtGui import QFont, QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QWidget
from PySide6.QtGui import QKeyEvent

class Terminal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.create_layout()
        self.create_processes()

    def create_widgets(self):
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setFont(QFont("Courier New"))

    def create_layout(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.text_edit)
        self.setCentralWidget(central_widget)

    def create_processes(self):
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_output)
        self.process.readyReadStandardError.connect(self.handle_error)
        self.process.started.connect(self.on_process_start)
        self.process.finished.connect(self.on_process_finish)
        self.process.setProcessChannelMode(QProcess.MergedChannels)

    def handle_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.text_edit.insertPlainText(output)

    def handle_error(self):
        error = self.process.readAllStandardError().data().decode()
        self.text_edit.insertPlainText(error)

    def on_process_start(self):
        self.text_edit.clear()

    def on_process_finish(self):
        self.text_edit.moveCursor(QTextCursor.End)
        self.text_edit.ensureCursorVisible()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return:
            command = self.text_edit.toPlainText().split("\n")[-1]
            self.process.write(command.encode())
            self.process.write("\n".encode())
            self.text_edit.moveCursor(QTextCursor.End)

    def start_terminal(self):
        if sys.platform == "win32":
            self.process.start("cmd")
        else:
            self.process.start("/bin/bash")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    terminal = Terminal()
    terminal.show()
    terminal.start_terminal()
    sys.exit(app.exec())
