from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "ClinCare API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Sistema de Gestión de Citas Médicas"

    DB_SERVER: str
    DB_PORT: int = 1433
    DB_NAME: str
    DB_DRIVER: str = "ODBC Driver 17 for SQL Server"
    DB_TRUSTED_CONNECTION: str = "yes"
    DB_TRUST_SERVER_CERTIFICATE: str = "yes"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def database_url(self) -> str:
        connection_string = (
            f"DRIVER={{{self.DB_DRIVER}}};"
            f"SERVER={self.DB_SERVER},{self.DB_PORT};"
            f"DATABASE={self.DB_NAME};"
            f"Trusted_Connection={self.DB_TRUSTED_CONNECTION};"
            f"TrustServerCertificate={self.DB_TRUST_SERVER_CERTIFICATE};"
        )
        return f"mssql+pyodbc:///?odbc_connect={quote_plus(connection_string)}"


settings = Settings()