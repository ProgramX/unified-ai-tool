from PySide6.QtGui import QFont

# Author: Mujtaba
# Date: July 4, 2023

# Description: Layout provider creates some layout/gui elements for other modules to access and use. It includes
# some buttons, menus and other gui elements that are used by other modules.

# TODO: MAJOR REFACTORING REQUIRED. THIS MODULE IS A MESS. -- EVERYTHING IS NAMED "menu" AND IT IS CONFUSING.

"""
todo: will make an identifier structure for each menu, and actions within menus. adding new menu items
shall be easy by using functions that add_to_menu(), add_under(), and so on.

only basic gui util is under the scope of this module. for functional operations, this module is
not responsible... note that this module does not create a single menu itself, but only provides
an interface for other modules to GUIfy their features.
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from editor.core import *

class LayoutProvider(Module):

    is_copilot_enabled: bool = True

    file_menu: QMenu
    tools_menu: QMenu
    support_menu: QMenu

    def _toggle_copilot_button(self, window):
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
        window.set_inner_widget(QWidget()) # replace by WelcomeScreenWidget

        # File menu
        self.file_menu = window.menubar.addMenu("File")
        self.file_menu.addAction("New")
        self.file_menu.addAction("Open")
        self.file_menu.addSeparator()
        self.file_menu.addAction("Preferences")
        self.file_menu.addSeparator()
        self.file_menu.addAction("Save")
        self.file_menu.addAction("Save as")
        self.file_menu.addSeparator()
        self.file_menu.addAction("Exit")

        # Tools menu
        self.tools_menu = window.menubar.addMenu("Tools")

        # Support us menu
        self.support_menu = window.menubar.addMenu("Support us")

        # Copilot button
        copilot_button = QPushButton("Copilot: Enabled", window.status_bar)
        copilot_button.setObjectName("enableCopilotButton")
        copilot_button.setStyleSheet("background-color: green; color: white; font-weight: bold")
        copilot_button.setFont(QFont("Arial", weight=QFont.Bold))  # Set the font weight to bold
        copilot_button.clicked.connect(lambda: self._toggle_copilot_button(window))
        window.status_bar.addPermanentWidget(copilot_button)

        actionsss = ["Scripting", "3D Modelling", "2D Drawing", "Image Generation", "Audio Synthesis", "Assistant", "Simple Chatbot"]
        for act in actionsss:
            window.toolbar.addAction(QAction(act, window.toolbar))


layout_provider = LayoutProvider("layout_provider")
print("module: layout_provider instanced")
