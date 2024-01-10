from pydantic_settings import BaseSettings, SettingsConfigDict

class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True)

    DB_USER: str = ""
    DB_PASSWORD: str = ""
    DB_HOST: str = ""
    DB_DATABASE: str = ""
    DB_PORT: str = "3306"

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"

environment = Environment()