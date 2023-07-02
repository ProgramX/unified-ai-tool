

# Author: Mujtaba
# Date: July 3, 2023

# Description: Provides a button for co-pilot provider modules to provide their services or not.

from editor.core import *
from PySide6.QtGui import QFont

class CopilotToggleModule(Module):

    is_copilot_enabled : bool = True # To be used by copilot provider modules to decide whether to provide or not

    def toggle_copilot_button(self, window):
        enable_copilot_button = window.status_bar.findChild(QPushButton, "enableCopilotButton")
        if enable_copilot_button.text() == "Copilot: Enabled":
            self.is_copilot_enabled = False
            enable_copilot_button.setText("Copilot: Disabled")
            enable_copilot_button.setStyleSheet("background-color: red; color: white; font-weight: bold")
        else:
            self.is_copilot_enabled = True
            enable_copilot_button.setText("Copilot: Enabled")
            enable_copilot_button.setStyleSheet("background-color: green; color: white; font-weight: bold")

    def on_window(self, window: MainWindow):
        copilot_button = QPushButton("Copilot: Enabled", window.status_bar)
        copilot_button.setObjectName("enableCopilotButton")
        copilot_button.setStyleSheet("background-color: green; color: white; font-weight: bold")
        copilot_button.setFont(QFont("Arial", weight=QFont.Bold))  # Set the font weight to bold
        copilot_button.clicked.connect(lambda: self.toggle_copilot_button(window))
        window.status_bar.addPermanentWidget(copilot_button)

copilot_toggle_module = CopilotToggleModule("copilot_toggle")
print("copilot_toggle module instanced")


