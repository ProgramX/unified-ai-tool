from editor.core import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class FileTreeView(QWidget):
    def __init__(self, workspace_path):
        super().__init__()

        self.file_tree_view = QTreeView()
        self.file_tree_view.setRootIsDecorated(False)
        self.file_tree_view.setAlternatingRowColors(True)
        self.file_tree_view.setSortingEnabled(True)
        self.file_tree_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.model = QFileSystemModel()
        self.model.setRootPath(workspace_path)
        self.file_tree_view.setModel(self.model)
        self.file_tree_view.setRootIndex(self.model.index(workspace_path))

        self.file_tree_view.clicked.connect(self.open_file)

        layout = QVBoxLayout(self)
        layout.addWidget(self.file_tree_view)

    def open_file(self, index):
        file_path = self.model.filePath(index)
        if not self.model.isDir(index):
            # Code to open the file goes here
            print("Opening file:", file_path)


class FileView(Module):
    workspace_path = ""  # Replace with the actual workspace path

    def on_window(self, window: MainWindow):
        # Add some action buttons such as create new file, open file, etc.
        new_file_button = QToolButton()
        new_file_button.setText("\U0001F4C4")
        new_file_button.setIconSize(QSize(32, 32))
        new_file_button.setFixedSize(32, 32)

        open_file_button = QToolButton()
        open_file_button.setText("\U0001F4C2")
        open_file_button.setIconSize(QSize(32, 32))
        open_file_button.setFixedSize(32, 32)

        delete_file_button = QToolButton()
        delete_file_button.setText("\U0001F5D1\ufe0f")
        delete_file_button.setIconSize(QSize(32, 32))
        delete_file_button.setFixedSize(32, 32)

        hbox = QHBoxLayout()
        hbox.addWidget(new_file_button)
        hbox.addWidget(open_file_button)
        hbox.addWidget(delete_file_button)
        window.left_sidebar.widgets.addLayout(hbox)

        fileview_widget: FileTreeView = FileTreeView(self.workspace_path)
        window.left_sidebar.widgets.addWidget(fileview_widget)


fileview = FileView("fileview_provider")
print("fileview_provider loaded")
