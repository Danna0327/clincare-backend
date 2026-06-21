from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_SERVER: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_DRIVER: str = "ODBC Driver 17 for SQL Server"

    APP_NAME: str = "ClinCare API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Sistema de Gestión de Citas Médicas"

    @property
    def database_url(self) -> str:
        driver = self.DB_DRIVER.replace(" ", "+")
        return (
            f"mssql+pyodbc://{self.DB_USERNAME}:{self.DB_PASSWORD}"
            f"@{self.DB_SERVER}/{self.DB_NAME}?driver={driver}"
        )

    class Config:
        env_file = ".env"


settings = Settings()