from editor.core import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class WelcomeWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        heading_label = QLabel("Welcome to Unified AI Tool")
        heading_font = QFont("Arial", 16, weight=QFont.Bold)
        heading_label.setFont(heading_font)
        layout.addWidget(heading_label)

        paragraph_label = QLabel(
            "This is a powerful tool that allows you to perform various AI-related tasks. "
            "Here are some key features:\n\n"
            "• Text-based features such as generating creative or technical text, or having a copilot help you write.\n"
            "• Image-based features such as image generation or editing based on AI-tools\n"
            "• 3D Modelling and rendering. Useful for 3D artists\n"
            "• Audio generation or editing and related features\n"
            "• And many more\n\n"
            "Start exploring and leveraging the capabilities of Unified AI Tool!"
        )
        layout.addWidget(paragraph_label)

        subheading_label = QLabel("Additional Information")
        subheading_font = QFont("Arial", 14, weight=QFont.Bold)
        subheading_label.setFont(subheading_font)
        layout.addWidget(subheading_label)

        additional_text_label = QLabel(
            "Unified AI Tool is developed and maintained by Muhammad Mujtaba on GitHub. "
            "You can contribute to its development by giving new ideas, funding, "
            "contributing to its development, or any means you believe is possible."
        )

        additional_text_label.setWordWrap(True)
        layout.addWidget(additional_text_label)

        button = QPushButton("Get Started")
        button.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(button)

        layout.addStretch()

        self.setLayout(layout)


class WelcomeScreen(Module):
    def open_provider_window(self, window: MainWindow):
        window.clear_right_sidebar()
        window.clear_status_bar()
        welcome_widget = WelcomeWidget()
        window.set_inner_widget(welcome_widget)

    def create_toolbar_entry(self, window: MainWindow):
        action = window.toolbar.addAction("\U0001F3E0 Welcome Screen")
        window.toolbar.addSeparator()
        action.triggered.connect(lambda: self.open_provider_window(window))

    def on_window(self, window: MainWindow):
        self.open_provider_window(window) # Welcome screen is open by default at start
        self.create_toolbar_entry(window)


welcome_screen = WelcomeScreen("welcome_screen")
print("welcome_screen loaded")
