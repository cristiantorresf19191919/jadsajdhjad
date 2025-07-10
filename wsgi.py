import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, '/home/abaqueroc/HouselyBackPython')

from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from app.main import app

# Create a WSGI application from the FastAPI app
application = app 