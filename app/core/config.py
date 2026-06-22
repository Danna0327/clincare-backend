from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # Configuración de Base de Datos
    # =========================
    db_server: str
    db_port: int = 1433
    db_name: str
    db_driver: str = "ODBC Driver 17 for SQL Server"

    # Opcional: usuario/clave si luego usas autenticación SQL
    db_user: str | None = None
    db_password: str | None = None

    # Si usas autenticación de Windows
    db_trusted_connection: bool = True

    # =========================
    # Configuración de la API
    # =========================
    app_name: str = "ClinCare API"
    app_version: str = "1.0.0"
    app_description: str = "Sistema de Gestión de Citas Médicas"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    @property
    def database_url(self) -> str:
        """
        Construye la URL de conexión para SQL Server.
        Compatible con autenticación de Windows o SQL Server.
        """
        driver = quote_plus(self.db_driver)

        # Si tienes usuario y contraseña, usa autenticación SQL
        if self.db_user and self.db_password:
            return (
                f"mssql+pyodbc://{self.db_user}:{self.db_password}"
                f"@{self.db_server}:{self.db_port}/{self.db_name}"
                f"?driver={driver}"
            )

        # Si no, usa autenticación de Windows
        return (
            f"mssql+pyodbc://@{self.db_server}:{self.db_port}/{self.db_name}"
            f"?driver={driver}&trusted_connection=yes"
        )


settings = Settings()