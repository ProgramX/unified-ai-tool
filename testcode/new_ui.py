import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QDockWidget, QTreeView,
    QFileSystemModel, QSplitter, QScrollArea, QWidget, QVBoxLayout, QToolBar
)
from PySide6.QtGui import Qt, QAction, QIcon
from PySide6.QtCore import Qt as QtCore, QUrl, QDir
from PySide6.QtGui import QDesktopServices


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Modern Flat GUI")
        self.setGeometry(100, 100, 800, 600)

        # Create the main splitter
        splitter = QSplitter(self)
        self.setCentralWidget(splitter)

        # Create the toolbar
        toolbar = QToolBar("Main Toolbar", self)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(toolbar)

        # Add actions to the toolbar
        actions = [
            ("Text", "path/to/text_icon.png"),
            ("Audio", "path/to/audio_icon.png"),
            ("Video", "path/to/video_icon.png"),
            ("Coding", "path/to/coding_icon.png"),
            ("Vector Art", "path/to/vector_icon.png"),
            ("Painting", "path/to/painting_icon.png"),
            ("3D Modelling", "path/to/3d_icon.png"),
            ("Mathematics", "path/to/math_icon.png"),
            ("Algorithms", "path/to/algo_icon.png"),
            ("Classification", "path/to/class_icon.png"),
            ("Documents", "path/to/doc_icon.png"),
            ("Images", "path/to/image_icon.png"),
            ("Scholar", "path/to/scholar_icon.png")
        ]

        for action_label, icon_path in actions:
            action = QAction(QIcon(icon_path), action_label, self)
            toolbar.addAction(action)

        # Create the top scrollable area for the top dock panel
        topScrollArea = QScrollArea()
        topScrollArea.setWidgetResizable(True)
        topScrollContent = QWidget(topScrollArea)
        topLayout = QVBoxLayout(topScrollContent)

        # Create the file model for the tree view
        fileModel = QFileSystemModel()
        fileModel.setRootPath("")
        fileModel.setFilter(QDir.AllEntries | QDir.Hidden)

        # Create the tree view for the file view
        treeView = QTreeView()
        treeView.setModel(fileModel)
        treeView.setRootIndex(fileModel.index(""))

        # Handle double-click events to open files
        treeView.doubleClicked.connect(self.openFile)

        # Add the tree view to the top layout
        topLayout.addWidget(treeView)
        topScrollArea.setWidget(topScrollContent)

        # Create the top dock panel and set the top scrollable area as its content
        topDock = QDockWidget("Top Dock", self)
        topDock.setAllowedAreas(QtCore.LeftDockWidgetArea | QtCore.RightDockWidgetArea)
        topDock.setWidget(topScrollArea)
        self.addDockWidget(QtCore.LeftDockWidgetArea, topDock)

        # Create the bottom scrollable area for the bottom dock panel
        bottomScrollArea = QScrollArea()
        bottomScrollArea.setWidgetResizable(True)
        bottomScrollContent = QWidget(bottomScrollArea)
        bottomLayout = QVBoxLayout(bottomScrollContent)
        bottomLayout.addWidget(QTextEdit("Bottom Scrollable Content"))
        bottomScrollArea.setWidget(bottomScrollContent)

        # Create the bottom dock panel and set the bottom scrollable area as its content
        bottomDock = QDockWidget("Bottom Dock", self)
        bottomDock.setAllowedAreas(QtCore.LeftDockWidgetArea | QtCore.RightDockWidgetArea)
        bottomDock.setWidget(bottomScrollArea)
        self.addDockWidget(QtCore.LeftDockWidgetArea, bottomDock)

        # Set the initial sizes for the dock panels
        splitter.setSizes([self.width() // 4, self.width() // 4, self.width() // 2])

    def openFile(self, index):
        file_path = self.sender().model().filePath(index)
        if file_path:
            # Open the file with the default associated application
            url = QUrl.fromLocalFile(file_path)
            QDesktopServices.openUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set global stylesheet for the application
    app.setStyleSheet('''
        QMainWindow {
            background-color: #f0f0f0;
        }

        QToolBar {
            background-color: #f0f0f0;
            border: none;
            spacing: 8px;
            padding: 4px;
        }

        QScrollArea {
            background-color: transparent;
            border: none;
            border-radius: 0;
            padding: 0;
            margin: 0;
            scrollbar-width: none;
        }

        QScrollArea > QWidget {
            background-color: transparent;
        }

        QDockWidget {
            background-color: #f0f0f0;
            border: none;
            font-size: 14px;
        }

        QTreeView {
            background-color: white;
            border: none;
            selection-background-color: #c7e1ff;
            alternate-background-color: #f0f0f0;
            font-size: 14px;
        }

        QTextEdit {
            background-color: white;
            border: 1px solid #d1d1d1;
            border-radius: 4px;
            font-size: 14px;
        }
    ''')

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
