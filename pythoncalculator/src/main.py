import importlib.machinery
import os
import re
import sys
sys.path.append(os.getcwd())

class BytecodeImporter(importlib.machinery.SourcelessFileLoader):
    def __init__(self, fullname, directory):
        # Ensure the directory path ends with a slash
        if not directory.endswith('/'):
            directory += '/'

        # Find the correct .pyc file with a version-specific suffix
        pyc_file = None
        for item in os.listdir(directory):
            if re.match(rf'{re.escape(fullname)}.cpython-\d{{2,}}.pyc', item):
                pyc_file = item
                break

        if pyc_file is None:
            raise FileNotFoundError(f"No .pyc file found for module '{fullname}'")

        print("FOUND IT " + directory + pyc_file)

        super().__init__(fullname, directory + pyc_file)

    def create_module(self, spec):
        return super().create_module(spec)

    def exec_module(self, module):
        super().exec_module(module)


# Print the current working directory
print("Current working directory:", os.getcwd())

# List all files and directories in the current working directory
print("Files and directories in '", os.getcwd(), "':")
for item in os.listdir(os.getcwd()):
    if os.path.isdir(item):
        print("Directory:", item)
    else:
        print("File:", item)

# Example usage
module_name = "runservice"  # Replace with your module name
loader = BytecodeImporter(module_name, "__pycache__")
spec = importlib.util.spec_from_loader(loader.name, loader)
module = importlib.util.module_from_spec(spec)
loader.exec_module(module)
