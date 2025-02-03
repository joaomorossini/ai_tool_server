# AI Tool Server

A FastAPI-based server for AI agent tools with OpenAPI 3.1.1 specification support.

## Features

- OpenAPI 3.1.1 compatibility
- API Key authentication
- Async operations support
- Extensive logging
- Docker deployment ready
- Easy extensibility through FastAPI routers

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and set your configuration:

   ```
   API_KEY=your-secure-api-key-here
   ```

3. Build and run with Docker:
   ```bash
   docker build -t ai-tool-server .
   docker run -p 8000:8000 --env-file .env ai-tool-server
   ```

## Development

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

Once running, access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Adding New Tools

1. Create a new router in `app/routers/`
2. Define your tool endpoints
3. Include the router in `main.py`

## Authentication

Include the API key in requests using the `X-API-Key` header:

```bash
curl -H "X-API-Key: your-api-key" http://localhost:8000/
```
