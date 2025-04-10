from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_user: str
    database_password: str
    database_host: str
    database_port: str
    database_name: str

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    
    class Config:
        env_file = ".env"
        # env_file_encoding = "utf-8"

settings = Settings()
  