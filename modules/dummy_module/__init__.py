

# Author: Mujtaba
# Date: July 2, 2023

# Description: Dummy plugin to test my plugin system.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
1. a module must not override anything, it must communicate with base modules dealing with
manaement of other modules to register itself. the API provided by the module-management module
must be used for seamless integration and registration of more modules.
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from editor.core import *

class DummyModule(Module):
    def on_window(self, window: MainWindow):
        text_editor = QPlainTextEdit()
        window.set_inner_widget(text_editor)

        file_menu = window.menubar.addMenu(self.name)
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")

# by convention, module name must be the name of directory of module. i want to enforce it
# but keeping it easy for now.
dummy_module = DummyModule("Scoobie File Nemu")
print("dummy Module instanced")

