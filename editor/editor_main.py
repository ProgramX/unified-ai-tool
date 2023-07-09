

# Author: Mujtaba
# Date: July 2, 2023

# Description: Loads editor core and plugins, and registers plugins with core.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from editor.core import *

from .styles import flat_light_mode, flat_dark_mode

# Get the list of files and directories in the plugins directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
module_dir = os.path.join(parent_dir, "modules")
modules = os.listdir(module_dir)

# Import all modules in the plugins directory
for this_module in modules:
    this_module_path = os.path.join(module_dir, this_module)
    if os.path.isdir(this_module_path) and "__init__.py" in os.listdir(this_module_path):
        module_name = this_module
        module = importlib.import_module(f"modules.{module_name}", package=__package__)
        # Now you can use the imported module as needed
        # For example: module.some_function()


def editor_main():
    app = QApplication(sys.argv)
    editor_window = MainWindow()
    editor_window.setStyleSheet(flat_dark_mode.flat_dark_mode_style)

    # After the core has been loaded, we load plugins:
    for _this_module in Module.modules:
        _this_module.on_window(editor_window)

    sys.exit(app.exec())