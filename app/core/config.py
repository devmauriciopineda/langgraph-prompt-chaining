from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    # Azure OpenAI
    azure_openai_api_key: str
    azure_openai_endpoint: str
    openai_api_version: str

    # Google GenAI
    google_api_key: str


settings = Settings()
