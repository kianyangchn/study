from pydantic_settings import BaseSettings


# === Settings ===
class Settings(BaseSettings):
    app_name: str = "Book Review API"
    debug: bool = False
    max_reviews: int = 100

    class Config:
        env_file = ".env"


settings = Settings()
