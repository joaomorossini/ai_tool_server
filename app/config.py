from pydantic_settings import BaseSettings
from pydantic import SecretStr
import os
from typing import ClassVar
from dotenv import load_dotenv

# Load the .env file explicitly
load_dotenv()

class Settings(BaseSettings):
    """Application settings."""
    
    # API Configuration
    api_key: str
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Logging Configuration
    log_level: str = "INFO"
    log_dir: str = "logs"
    
    # Replace class Config with ConfigDict
    ConfigDict: ClassVar = {
        "env_file": ".env",
        "case_sensitive": False
    }

    # Apply ConfigDict using model_config
    model_config = ConfigDict

    # Remove ConfigDict
    # ConfigDict: ClassVar = {
    #     "env_file": ".env",
    #     "case_sensitive": False
    # } 
