
from modules.dummy_module import *

class AccessorModule(Module):
    def on_window(self, window: MainWindow):
        window.status_bar.showMessage("This data is accessed from module: " + dummy_module.name)


accessor_module = AccessorModule("Accessor Module")
print("Accessor module called")