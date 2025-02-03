from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from typing import Annotated
import os
from datetime import datetime

from .config import Settings

# Initialize settings
settings = Settings()

# Configure logger
logger.add(
    f"logs/tool_server_{datetime.now().strftime('%Y%m%d')}.log",
    rotation="500 MB",
    level="INFO"
)

# Initialize FastAPI app
app = FastAPI(
    title="AI Tool Server",
    description="API server for AI agent tools",
    version="1.0.0",
    openapi_version="3.1.1"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Key authentication
# api_key_header = APIKeyHeader(name="X-API-Key")

# Remove the verify_api_key function
# async def verify_api_key(api_key: Annotated[str, Security(api_key_header)]):
#     """Verify the API key against the configured value."""
#     if api_key != settings.api_key:
#         logger.warning(f"Invalid API key attempt: {api_key[:10]}...")
#         raise HTTPException(
#             status_code=403,
#             detail="Invalid API key"
#         )
#     return api_key

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/")
async def root():
    """Root endpoint without authentication."""
    return {"message": "Welcome to the AI Tool Server"}

# Import and include routers
# from .routers import tools
# app.include_router(tools.router, prefix="/tools", tags=["tools"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=4
    ) 
