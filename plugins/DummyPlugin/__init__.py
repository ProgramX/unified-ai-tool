

# Author: Mujtaba
# Date: July 2, 2023

# Description: Dummy plugin to test my plugin system.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from editor.core import *

class DummyPlugin(Plugin):
    def on_window(self, window: MainWindow):
        file_menu = window.menubar.addMenu(self.name)
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")

DummyPlugin("Scoobie File Nemu")
print("Module called")