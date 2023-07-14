
# Run it to resolve all external dependencies before running the _init__.py
# For dependencies between modules, we need to write script, or use some kind
# of protocol to detect what modules are using what other modules.

import subprocess

packages = [
    "pyside6",
    "python-magic-bin",
    "package3"
]  # Add more package names as needed

for package in packages:
    try:
        subprocess.check_call(["pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}: {e}")
