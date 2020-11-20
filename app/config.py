from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DRIVER: str = "postgres"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = 5432

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
