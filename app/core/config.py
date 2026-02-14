from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    ENV: str
    APP_NAME: str
    API_PREFIX: str
    CORS_ORIGINS: str
    LOG_LEVEL: str
    
    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]
   

settings = Settings()