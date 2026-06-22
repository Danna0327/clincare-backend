from typing import Optional
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # Configuración de Base de Datos
    # =========================
    DB_TYPE: str = "sqlite"
    DB_SERVER: Optional[str] = None
    DB_PORT: int = 1433
    DB_NAME: str = "clincare_db"
    DB_DRIVER: str = "ODBC Driver 17 for SQL Server"

    # Opcional: usuario/clave si luego usas autenticación SQL
    DB_USER: Optional[str] = None
    DB_PASSWORD: Optional[str] = None

    # Si usas autenticación de Windows
    DB_TRUSTED_CONNECTION: str = "yes"
    DB_TRUST_SERVER_CERTIFICATE: str = "yes"

    # =========================
    # Configuración de la API
    # =========================
    APP_NAME: str = "ClinCare API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Sistema de Gestión de Citas Médicas"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    @property
    def database_url(self) -> str:
        """
        Construye la URL de conexión para la base de datos.
        Si DB_TYPE=sqlite, usa una base de datos local.
        Si DB_TYPE=sqlserver, usa SQL Server con pyodbc.
        """
        if self.DB_TYPE.lower() == "sqlite":
            return "sqlite:///./database/clincare.db"

        driver = quote_plus(self.DB_DRIVER)

        if self.DB_USER and self.DB_PASSWORD:
            return (
                f"mssql+pyodbc://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_SERVER}:{self.DB_PORT}/{self.DB_NAME}"
                f"?driver={driver}"
            )

        return (
            f"mssql+pyodbc://@{self.DB_SERVER}:{self.DB_PORT}/{self.DB_NAME}"
            f"?driver={driver}&trusted_connection={self.DB_TRUSTED_CONNECTION}"
            f"&trustservercertificate={self.DB_TRUST_SERVER_CERTIFICATE}"
        )


settings = Settings()