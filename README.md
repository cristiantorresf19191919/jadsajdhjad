# Housely Property Management API

A FastAPI-based REST API for managing property information with in-memory storage.

## Features

- 🏠 Property management with full CRUD operations
- 📍 Store property details including location, address, pricing, rooms, bathrooms, and area
- 💾 In-memory database simulation
- 🔍 Health check endpoint
- 📚 Beautiful HTML interface for server validation
- 🚀 FastAPI with automatic API documentation

## Property Information Fields

- **name**: Property name
- **address**: Property address
- **price_range**: Price range (e.g., "$200,000 - $250,000")
- **rooms**: Number of rooms
- **bathrooms**: Number of bathrooms
- **area_m2**: Area in square meters
- **location**: Location/neighborhood
- **description**: Property description

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server with:
```bash
fastapi dev main.py
```

Or alternatively:
```bash
uvicorn main:app --reload
```

Or using the run script:
```bash
python run.py
```

The API will be available at:
- **Main Interface**: http://localhost:8000/
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## API Endpoints

### Health Check
- `GET /health` - Check server status

### Properties
- `GET /properties` - Get all properties
- `GET /properties/{id}` - Get property by ID
- `POST /properties` - Create new property
- `PUT /properties/{id}` - Update property
- `DELETE /properties/{id}` - Delete property

## Example Usage

### Create a Property
```bash
curl -X POST "http://localhost:8000/properties/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Modern Downtown Apartment",
    "address": "123 Main St, Downtown",
    "price_range": "$300,000 - $350,000",
    "rooms": 2,
    "bathrooms": 2,
    "area_m2": 85.5,
    "location": "Downtown",
    "description": "Beautiful modern apartment with city views"
  }'
```

### Get All Properties
```bash
curl -X GET "http://localhost:8000/properties/"
```

### Get Property by ID
```bash
curl -X GET "http://localhost:8000/properties/1"
```

### Update Property
```bash
curl -X PUT "http://localhost:8000/properties/1" \
  -H "Content-Type: application/json" \
  -d '{
    "price_range": "$320,000 - $370,000",
    "description": "Updated description"
  }'
```

### Delete Property
```bash
curl -X DELETE "http://localhost:8000/properties/1"
```

## Project Structure

```
HouselyBack/
├── main.py                  # FastAPI application entry point
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── property.py      # Property data models
│   ├── code/
│   │   ├── __init__.py
│   │   └── database.py      # In-memory database service
│   └── routers/
│       ├── __init__.py
│       ├── health.py        # Health check endpoints
│       └── properties.py    # Property CRUD endpoints
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running FastAPI applications
- **HTML/CSS**: Beautiful interface for the root endpoint

## Development

The application uses an in-memory database that resets when the server restarts. For production use, consider implementing a persistent database like PostgreSQL or SQLite.
