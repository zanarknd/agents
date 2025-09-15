from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class IpApiSettings(BaseModel):
    host: str


class ClientsSettings(BaseModel):
    ipapi: IpApiSettings


class Settings(BaseSettings):
    clients: ClientsSettings

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_nested_delimiter="_",
    )


if __name__ == "__main__":
    settings = Settings()
    print(settings.clients.ipapi)
