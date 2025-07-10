import sys
import os

# Add the project directory to the Python path
project_home = '/home/abaqueroc/HouselyBackPython'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Change to the project directory
os.chdir(project_home)

try:
    from main import app
    application = app
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Current sys.path: {sys.path}")
    print(f"Current working directory: {os.getcwd()}")
    raise 