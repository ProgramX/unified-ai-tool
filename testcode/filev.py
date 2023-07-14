import os
import sys
from pathlib import Path
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTreeView, QVBoxLayout, QWidget, QApplication


class FileViewerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("File Viewer")

        # Create the model to hold the file hierarchy
        self.model = QStandardItemModel()

        # Create the tree view to display the file hierarchy
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIsDecorated(False)
        self.tree_view.setHeaderHidden(True)
        self.tree_view.doubleClicked.connect(self.handle_file_clicked)

        # Create the layout and add the tree view
        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)
        self.setLayout(layout)

    def load_file_hierarchy(self, root_directory):
        # Clear the existing model
        self.model.clear()

        # Set up the root item
        root_item = QStandardItem(root_directory)
        self.model.appendRow(root_item)

        # Recursively populate the model with the file hierarchy
        self.populate_model(root_item, root_directory)

    def populate_model(self, parent_item, directory):
        # Retrieve the list of files and directories within the given directory
        file_list = self.get_file_list(directory)

        for file_name in file_list:
            file_item = QStandardItem(file_name)
            parent_item.appendRow(file_item)

            # If the item represents a directory, recursively populate its children
            if self.is_directory(os.path.join(directory, file_name)):
                child_directory = os.path.join(directory, file_name)
                self.populate_model(file_item, child_directory)

    def handle_file_clicked(self, index):
        # Retrieve the file name from the clicked index
        file_name = self.model.itemFromIndex(index).text()
        file_path = self.join_paths(self.get_current_directory(), file_name)

        # Perform the desired action on the clicked file
        self.handle_file_clicked(file_path)

    def get_current_directory(self):
        # Retrieve the directory path of the currently selected item
        index = self.tree_view.currentIndex()
        item = self.model.itemFromIndex(index)
        directory = item.text()

        # Traverse up the tree to get the full directory path
        parent = item.parent()
        while parent is not None:
            directory = self.join_paths(parent.text(), directory)
            parent = parent.parent()

        return directory

    def get_file_list(self, directory):
        # Retrieve the list of files and directories within the given directory
        file_list = []
        for file_name in os.listdir(directory):
            if not file_name.startswith('.'):  # Skip hidden files
                file_list.append(file_name)
        return file_list

    def is_directory(self, path):
        # Check if the given path is a directory
        return os.path.isdir(path)

    def join_paths(self, path1, path2):
        # Join two paths together
        return os.path.join(path1, path2)

    def handle_file_clicked(self, file_path):
        # Perform the desired action on the clicked file
        print("Clicked file:", file_path)
        # Add your code here to handle the clicked file


app = QApplication(sys.argv)
file_viewer = FileViewerWidget()
file_viewer.load_file_hierarchy("E:/projects")
file_viewer.show()
sys.exit(app.exec())
