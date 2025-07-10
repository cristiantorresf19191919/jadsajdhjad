from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers import properties, health

app = FastAPI(
    title="Housely Property Management API",
    description="A REST API for managing property information",
    version="1.0.0"
)

# Include routers
app.include_router(health.router)
app.include_router(properties.router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    """Root endpoint with beautiful HTML interface for health check validation"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Housely Property Management API</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                padding: 40px;
                max-width: 800px;
                width: 100%;
                text-align: center;
            }
            
            .logo {
                font-size: 3rem;
                font-weight: bold;
                color: #667eea;
                margin-bottom: 20px;
            }
            
            .status {
                background: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 25px;
                display: inline-block;
                margin: 20px 0;
                font-weight: bold;
            }
            
            .description {
                color: #666;
                margin-bottom: 30px;
                line-height: 1.6;
            }
            
            .endpoints {
                background: #f8f9fa;
                border-radius: 10px;
                padding: 20px;
                margin: 20px 0;
                text-align: left;
            }
            
            .endpoint {
                margin: 10px 0;
                padding: 10px;
                background: white;
                border-radius: 5px;
                border-left: 4px solid #667eea;
            }
            
            .method {
                font-weight: bold;
                color: #667eea;
            }
            
            .url {
                color: #333;
                font-family: monospace;
            }
            
            .docs-link {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 15px 30px;
                text-decoration: none;
                border-radius: 25px;
                margin-top: 20px;
                font-weight: bold;
                transition: transform 0.2s;
            }
            
            .docs-link:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">🏠 Housely</div>
            <div class="status">✅ Server is Running</div>
            <p class="description">
                Welcome to the Housely Property Management API! This is a REST API designed to help you manage property information including location, pricing, rooms, bathrooms, and more.
            </p>
            
            <div class="endpoints">
                <h3>Available Endpoints:</h3>
                <div class="endpoint">
                    <span class="method">GET</span> <span class="url">/health</span> - Health check
                </div>
                <div class="endpoint">
                    <span class="method">GET</span> <span class="url">/properties</span> - Get all properties
                </div>
                <div class="endpoint">
                    <span class="method">GET</span> <span class="url">/properties/{id}</span> - Get property by ID
                </div>
                <div class="endpoint">
                    <span class="method">POST</span> <span class="url">/properties</span> - Create new property
                </div>
                <div class="endpoint">
                    <span class="method">PUT</span> <span class="url">/properties/{id}</span> - Update property
                </div>
                <div class="endpoint">
                    <span class="method">DELETE</span> <span class="url">/properties/{id}</span> - Delete property
                </div>
            </div>
            
            <a href="/docs" class="docs-link">📚 View API Documentation</a>
        </div>
    </body>
    </html>
    """
    return html_content 