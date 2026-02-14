from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    ENV: str
    APP_NAME: str
    API_PREFIX: str
    CORS_ORIGINS: str
    LOG_LEVEL: str
    

   

settings = Settings()
