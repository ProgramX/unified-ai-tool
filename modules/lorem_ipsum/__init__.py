
# A dummy module to fill GUI elements, to have something to look at.

from editor.core import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class LoremIpsum(Module):

    def on_ready(self, window: MainWindow):
        window.menubar.addMenu("File")
        window.menubar.addMenu("Edit")
        window.menubar.addMenu("View")
        window.menubar.addMenu("Help")
        window.menubar.addMenu("Tools")
        window.menubar.addMenu("Window")
        window.menubar.addMenu("Settings")
        window.menubar.addMenu("Plugins")
        window.menubar.addMenu("About")
        window.menubar.addMenu("Lorem Ipsum")


lorem_ipsum = LoremIpsum("welcome_screen")
print("lorem_ipsum loaded")
