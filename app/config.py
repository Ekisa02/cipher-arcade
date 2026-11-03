from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Cipher Arcade"
    model_path: str = "model.pt"

settings = Settings()
