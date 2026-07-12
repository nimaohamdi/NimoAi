from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # Application
    # =========================
    APP_NAME: str = "NimoAI"
    VERSION: str = "2.3.0"

    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    DEBUG: bool = True

    # =========================
    # Security
    # =========================
    ALLOWED_ORIGINS: list[str] = ["*"]

    # =========================
    # AI Provider
    # =========================
    BASE_URL: str = "https://api.gapgpt.app/v1"
    API_KEY: str = ""

    DEFAULT_MODEL: str = "gpt-4o-mini"

    REQUEST_TIMEOUT: int = 120

    # =========================
    # Future
    # =========================
    OLLAMA_URL: str = "http://localhost:11434"

    ENABLE_MEMORY: bool = False
    ENABLE_STREAM: bool = True

    DATABASE_URL: str = "sqlite:///nimo.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )

DEFAULT_PROVIDER: str = "gapgpt"
DEFAULT_MODEL: str = "gpt-4o-mini"

settings = Settings()