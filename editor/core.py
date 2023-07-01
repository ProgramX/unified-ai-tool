
# Author: Mujtaba
# Date: July 2, 2023

# Editor Core - instanced and called by the program. It triggers all plugins to load their
# stuff into the program GUI.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import importlib

import sys
from abc import abstractmethod

from PySide6.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QMainWindow, QMenu, QToolBar, QVBoxLayout, \
    QGridLayout, QWidget, QLabel, QPushButton, QDockWidget, QTextEdit, QSplitter, QStatusBar, QScrollArea, \
    QPlainTextEdit, QMenuBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QCursor


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)


class ToolBar(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)


class LeftDockBar(QDockWidget):

    widgets: QVBoxLayout # left_sidebar_layout

    def __init__(self, parent):
        super().__init__("LeftDockBar", parent)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        left_sidebar_widget = QWidget()
        self.widgets = QVBoxLayout()
        left_sidebar_widget.setLayout(self.widgets)

        left_scroll_area = QScrollArea()
        left_scroll_area.setWidgetResizable(True)
        left_scroll_area.setWidget(left_sidebar_widget)

        self.setWidget(left_scroll_area)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)  # Disable moving or closing


class RightDockBar(QDockWidget):

    widgets: QVBoxLayout # right_sidebar_layout

    def __init__(self, parent):
        super().__init__("RightDockBar", parent)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        right_sidebar_widget = QWidget()
        self.widgets = QVBoxLayout()
        right_sidebar_widget.setLayout(self.widgets)

        left_scroll_area = QScrollArea()
        left_scroll_area.setWidgetResizable(True)
        left_scroll_area.setWidget(right_sidebar_widget)

        self.setWidget(left_scroll_area)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)  # Disable moving or closing


class BottomDockBar(QDockWidget):
    def __init__(self, parent):
        super().__init__("BottomDockBar", parent)
        self.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)


class StatusBar(QStatusBar):
    def __init__(self):
        super().__init__()



class MainWindow(QMainWindow):
    menubar: MenuBar
    toolbar: ToolBar

    bottom_bar: BottomDockBar
    status_bar: QStatusBar

    left_sidebar: LeftDockBar
    right_sidebar: RightDockBar

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set flat style for all widgets
        QApplication.setStyle("fusion")
        QApplication.setPalette(QApplication.style().standardPalette())

        self.menubar = MenuBar(self)
        self.setMenuBar(self.menubar)

        self.toolbar = ToolBar(self)
        self.addToolBar(self.toolbar)

        self.left_sidebar = LeftDockBar(self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.left_sidebar)

        self.right_sidebar = RightDockBar(self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.right_sidebar)

        text_editor = QTextEdit()
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.left_sidebar)
        splitter.addWidget(text_editor)
        splitter.addWidget(self.right_sidebar)
        splitter.setSizes([self.width() // 4, self.width() * 3 // 4, self.width() // 4])

        self.setCentralWidget(splitter)

        self.bottom_bar = BottomDockBar(self)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.bottom_bar)

        self.status_bar = StatusBar()
        self.setStatusBar(self.status_bar)

        self.setGeometry(64, 64, 1320, 600)
        self.setWindowTitle("Unified AI Tool")
        self.show()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Plugin:
    plugins = [] # static variable holding list of all plugins

    name : str # Unique name of this plugin

    def __init__(self, name):
        for plugin in Plugin.plugins:
            if plugin.name == name:
                print("Warning: Misbehaviour may occur since plugin with name " + plugin.name + " already exists.")
                print("If you are creating a new plugin, consider changing its name.")

        self.name = name
        Plugin.plugins.append(self)

    """
    param `window` in following function can be used in overriding functions as:
    1. window.menubar.addMenu("Name")

    2. action_menu = QAction("Menu", window.toolbar)
       window.toolbar.addAction(action_menu)

    3. terminal = QPlainTextEdit()
       window.bottom_bar.setWidget(terminal)

    4. window.left_sidebar.widgets.addWidget(option)
       window.right_sidebar.widgets.addWidget(option)

    5. window.status_bar.SOMESHIT OR
       window.statusBar().addPermanentWidget(enable_copilot_button)
    """
    @abstractmethod
    def on_window(self, window: MainWindow):
        pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #





