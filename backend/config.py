from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Nimo AI"
    VERSION: str = "2.3.0"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # امنیت
    ALLOWED_ORIGINS: list = ["*"]  # بعداً محدودش کن
    
    class Config:
        env_file = ".env"

settings = Settings()