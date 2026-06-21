from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "ClinCare API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Sistema de Gestión de Citas Médicas"

    DB_SERVER: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_DRIVER: str = "ODBC Driver 17 for SQL Server"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def database_url(self) -> str:
        driver = self.DB_DRIVER.replace(" ", "+")
        return (
            f"mssql+pyodbc://{self.DB_USERNAME}:{self.DB_PASSWORD}"
            f"@{self.DB_SERVER}/{self.DB_NAME}?driver={driver}"
        )


settings = Settings()