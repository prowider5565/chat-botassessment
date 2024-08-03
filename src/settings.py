from pydantic import Field, AnyHttpUrl, validator
import enum
from pathlib import Path
from tempfile import gettempdir
from typing import Optional, List

from pydantic_settings import BaseSettings
from yarl import URL

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    HOST: str
    PORT: int
    # Quantity of workers for uvicorn
    # Enable uvicorn reloading
    RELOAD: bool = False

    # Current environment
    ENVIRONMENT: str
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_NAME: str
    MONGO_TZ_AWARE: bool
    LOG_PATH: str = "../logs/debug.log"
    IMAGE_DIR: str = "src/media"

    BOT_TOKEN: str

    class Config:
        env_file = ".env"


settings = Settings()
