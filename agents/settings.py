from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class IpApiSettings(BaseModel):
    host: str


class ClientsSettings(BaseModel):
    ipapi: IpApiSettings


class Settings(BaseSettings):
    clients: ClientsSettings
    user_agent: str

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_nested_delimiter="_",
    )


settings = Settings()

if __name__ == "__main__":
    print(settings)
