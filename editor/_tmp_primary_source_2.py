import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QMainWindow, QMenu, QToolBar, QVBoxLayout, \
    QGridLayout, QWidget, QLabel, QPushButton, QDockWidget, QTextEdit, QSplitter, QStatusBar, QScrollArea, \
    QPlainTextEdit, QMenuBar
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


class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        # File menu
        file_menu = self.addMenu("File")
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")

        # Options menu
        options_menu = self.addMenu("Options")
        options_menu.addAction("Preferences")
        options_menu.addAction("Settings")

        # Tools menu
        tools_menu = self.addMenu("Tools")
        tools_menu.addAction("Calculator")
        tools_menu.addAction("Notepad")
        tools_menu.addAction("Terminal")

        # Extensions menu
        extensions_menu = self.addMenu("Extensions")
        extensions_menu.addAction("Plugin 1")
        extensions_menu.addAction("Plugin 2")

        # Support us menu
        support_menu = self.addMenu("Support us")
        support_menu.addAction("Donate")
        support_menu.addAction("Feedback")


class ToolBar(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)

        # Create the first action as an icon menu button
        action_menu = QAction(QIcon("../assets/1x_icons/down.png"), "Menu", self)
        action_menu.triggered.connect(self.parent().openListMenu)
        self.addAction(action_menu)

        self.addSeparator()
        self.addSeparator()

        # Add the rest of the actions in the center of the toolbar
        for i in range(1, 11):
            action = QAction(f"Action {i}", self)
            self.addAction(action)


class BottomDockBar(QDockWidget):
    def __init__(self, parent):
        super().__init__("Terminal", parent)
        self.setAllowedAreas(Qt.BottomDockWidgetArea)
        terminal = QPlainTextEdit()
        self.setWidget(terminal)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)


class LeftDockBar(QDockWidget):
    def __init__(self, parent):
        super().__init__("Tools", parent)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
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

        self.setWidget(left_scroll_area)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)  # Disable moving or closing


class RightDockBar(QDockWidget):
    def __init__(self, parent):
        super().__init__("Options", parent)
        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
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

        self.setWidget(right_scroll_area)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)  # Disable moving or closing


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def openListMenu(self):
        menu = QMenu(self)

        num_items = 20  # Number of menu items

        for index in range(1, num_items + 1):
            action = QAction(f"Menu Option {index}", self)
            action.setIcon(QIcon("../assets/1x_icons/wrench.png"))  # Set the icon
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

        menubar = MenuBar(self)
        self.setMenuBar(menubar)

        toolbar = ToolBar(self)
        self.addToolBar(toolbar)

        left_sidebar = LeftDockBar(self)
        self.addDockWidget(Qt.LeftDockWidgetArea, left_sidebar)

        right_sidebar = RightDockBar(self)
        self.addDockWidget(Qt.RightDockWidgetArea, right_sidebar)

        text_editor = QTextEdit()
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_sidebar)
        splitter.addWidget(text_editor)
        splitter.addWidget(right_sidebar)
        splitter.setSizes([self.width() // 4, self.width() * 3 // 4, self.width() // 4])

        self.setCentralWidget(splitter)

        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Status message goes here")

        bottom_bar = BottomDockBar(self)
        self.addDockWidget(Qt.BottomDockWidgetArea, bottom_bar)

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
