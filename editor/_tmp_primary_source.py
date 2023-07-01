
# Author: Mujtaba
# Date: July 1, 2023

# Dummy GUI for Unified AI Tool. It will act as a precursor to real GUI.

import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QMainWindow, QMenu, QToolBar, QVBoxLayout, QGridLayout, QWidget, QLabel, QPushButton, QDockWidget, QTextEdit, QSplitter, QStatusBar, QScrollArea, QPlainTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QCursor


class SidebarOption(QWidget):
    def __init__(self, label):
        super().__init__()
        self.initUI(label)

    def initUI(self, label):
        layout = QVBoxLayout()  # Use QVBoxLayout for the main layout
        self.setLayout(layout)

        label_widget = QLabel(label)
        layout.addWidget(label_widget)

        row_layout = QHBoxLayout()  # Use QHBoxLayout for the row containing QLineEdit and QPushButton
        layout.addLayout(row_layout)

        input_widget = QLineEdit()
        row_layout.addWidget(input_widget)

        add_button = QPushButton("ADD")
        row_layout.addWidget(add_button)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    """
    def openPanelMenu(self):
        menu = QMenu(self)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QGridLayout()
        scroll_widget.setLayout(scroll_layout)

        num_rows = 16
        num_cols = 4

        for row in range(num_rows):
            for col in range(num_cols):
                index = row * num_cols + col + 1
                if index <= 20:  # Limit the number of menu items to 20
                    action = QAction(f"Menu Option {index}", self)
                    action.triggered.connect(self.menuOptionClicked)
                    scroll_layout.addWidget(QPushButton(f"Option {index}"), row, col)

        scroll_area.setWidget(scroll_widget)
        menu.setFixedWidth(scroll_area.sizeHint().width() + scroll_area.verticalScrollBar().sizeHint().width() * 4)
        menu.setFixedHeight(scroll_area.sizeHint().height() + scroll_area.horizontalScrollBar().sizeHint().height() * 8)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        menu.setLayout(QVBoxLayout())
        menu.layout().addWidget(scroll_area)

        menu.exec(QCursor.pos())

    def menuOptionClicked(self):
        action = self.sender()
        print(f"Menu option clicked: {action.text()}")
    """


    def openListMenu(self):
        menu = QMenu(self)

        num_items = 20  # Number of menu items

        for index in range(1, num_items + 1):
            action = QAction(f"Menu Option {index}", self)
            action.triggered.connect(self.menuOptionClicked)
            menu.addAction(action)

        menu.exec(QCursor.pos())


    def menuOptionClicked(self):
        action = self.sender()
        print(f"Menu option clicked: {action.text()}")

    def toggleCopilot(self):
        enable_copilot_button = self.findChild(QPushButton, "enableCopilotButton")
        if enable_copilot_button.text() == "Copilot: Enabled":
            enable_copilot_button.setText("Copilot: Disabled")
            enable_copilot_button.setStyleSheet("background-color: red")
        else:
            enable_copilot_button.setText("Copilot: Enabled")
            enable_copilot_button.setStyleSheet("background-color: green")

    def initUI(self):
        # Set flat style for all widgets
        QApplication.setStyle("fusion")
        QApplication.setPalette(QApplication.style().standardPalette())

        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")

        # Options menu
        options_menu = menubar.addMenu("Options")
        options_menu.addAction("Preferences")
        options_menu.addAction("Settings")

        # Tools menu
        tools_menu = menubar.addMenu("Tools")
        tools_menu.addAction("Calculator")
        tools_menu.addAction("Notepad")
        tools_menu.addAction("Terminal")

        # Extensions menu
        extensions_menu = menubar.addMenu("Extensions")
        extensions_menu.addAction("Plugin 1")
        extensions_menu.addAction("Plugin 2")

        # Support us menu
        support_menu = menubar.addMenu("Support us")
        support_menu.addAction("Donate")
        support_menu.addAction("Feedback")

        # Toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Create the first action as an icon menu button
        action_menu = QAction(QIcon("../assets/1x_icons/down.png"), "Menu", self)
        action_menu.triggered.connect(self.openListMenu)
        toolbar.addAction(action_menu)

        toolbar.addSeparator()
        toolbar.addSeparator()

        # Add the rest of the actions in the center of the toolbar
        for i in range(1, 11):
            action = QAction(f"Action {i}", self)
            toolbar.addAction(action)

        # Left Sidebar
        left_sidebar = QDockWidget("Tools", self)
        left_sidebar.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        left_sidebar_widget = QWidget()
        left_sidebar_layout = QVBoxLayout()
        left_sidebar_widget.setLayout(left_sidebar_layout)

        # Add 20 left sidebar options to demonstrate scrolling
        for i in range(1, 21):
            option = SidebarOption(f"Option {i}")
            left_sidebar_layout.addWidget(option)

        left_scroll_area = QScrollArea()
        left_scroll_area.setWidgetResizable(True)
        left_scroll_area.setWidget(left_sidebar_widget)

        left_sidebar.setWidget(left_scroll_area)
        left_sidebar.setFeatures(QDockWidget.NoDockWidgetFeatures)  # Disable moving or closing

        # Right Sidebar
        right_sidebar = QDockWidget("Options", self)
        right_sidebar.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        right_sidebar_widget = QWidget()
        right_sidebar_layout = QVBoxLayout()
        right_sidebar_widget.setLayout(right_sidebar_layout)

        # Add 10 right sidebar options to demonstrate scrolling
        for i in range(1, 11):
            option = SidebarOption(f"Option {i}")
            right_sidebar_layout.addWidget(option)

        right_scroll_area = QScrollArea()
        right_scroll_area.setWidgetResizable(True)
        right_scroll_area.setWidget(right_sidebar_widget)

        right_sidebar.setWidget(right_scroll_area)
        right_sidebar.setFeatures(QDockWidget.NoDockWidgetFeatures)  # Disable moving or closing

        # Text Editor
        text_editor = QTextEdit()

        # Create a splitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_sidebar)
        splitter.addWidget(text_editor)
        splitter.addWidget(right_sidebar)
        splitter.setSizes([self.width() // 4, self.width() * 3 // 4, self.width() // 4])

        # Set the splitter as the central widget
        self.setCentralWidget(splitter)

        # Status bar
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Status message goes here")

        # Bottom bar (Terminal)

        bottom_bar = QDockWidget("Terminal", self)
        bottom_bar.setAllowedAreas(Qt.BottomDockWidgetArea)
        terminal = QPlainTextEdit()
        bottom_bar.setWidget(terminal)
        bottom_bar.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.BottomDockWidgetArea, bottom_bar)

        # Enable Copilot button
        enable_copilot_button = QPushButton("Copilot: Enabled", self)
        enable_copilot_button.setObjectName("enableCopilotButton")
        enable_copilot_button.setStyleSheet("background-color: green")
        enable_copilot_button.clicked.connect(self.toggleCopilot)
        self.statusBar().addPermanentWidget(enable_copilot_button)

        self.setGeometry(64, 64, 1320, 600)
        self.setWindowTitle("Unified AI Tool")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
