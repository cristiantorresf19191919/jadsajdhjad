import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, '/home/abaqueroc/HouselyBackPython')

from main import app

# Export the application for WSGI
application = app