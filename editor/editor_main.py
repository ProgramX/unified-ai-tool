

# Author: Mujtaba
# Date: July 2, 2023

# Description: Loads editor core and plugins, and registers plugins with core.


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from editor.core import *


# Get the list of files and directories in the plugins directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plugin_dir = os.path.join(parent_dir, "plugins")
plugins = os.listdir(plugin_dir)

# Import all modules in the plugins directory
for plugin in plugins:
    plugin_path = os.path.join(plugin_dir, plugin)
    if os.path.isdir(plugin_path) and "__init__.py" in os.listdir(plugin_path):
        module_name = plugin
        module = importlib.import_module(f"plugins.{module_name}", package=__package__)
        # Now you can use the imported module as needed
        # For example: module.some_function()


def editor_main():
    app = QApplication(sys.argv)
    editor_window = MainWindow()

    # After the core has been loaded, we load plugins:
    for plugin in Plugin.plugins:
        plugin.on_window(editor_window)

    sys.exit(app.exec())