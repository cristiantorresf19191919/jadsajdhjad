import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, '/home/abaqueroc/HouselyBackPython')

from main import app
from fastapi.middleware.wsgi import WSGIMiddleware

# Create a WSGI application using WSGIMiddleware
application = WSGIMiddleware(app) 