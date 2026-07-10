from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ==========================
    # Application
    # ==========================
    APP_NAME: str = "Single Agent AI Research Assistant"
    DEBUG: bool = True

    # ==========================
    # Logging
    # ==========================
    LOG_LEVEL: str = "INFO"

    
    # ==========================
    # LLM Configuration
    # # ==========================
    # LLM_PROVIDER: str = "groq"
    LLM_MODEL: str = "llama-3.3-70b-versatile"
    GROQ_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    LLM_TEMPERATURE: float = 0.2
    LLM_MAX_TOKENS: int = 2000
    
    # ==========================
    # Runtime
    # ==========================
    REQUEST_TIMEOUT: int = 60
    MAX_RETRIES: int = 3

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()