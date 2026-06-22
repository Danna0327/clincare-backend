from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

engine_kwargs = {}
if settings.database_url.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(
    settings.database_url,
    echo=False,
    future=True,
    **engine_kwargs,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_database_connection() -> bool:
    """
    Verifica si existe conexión con la base de datos.
    Retorna True si la conexión es exitosa, caso contrario False.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except SQLAlchemyError as e:
        print(f"[ClinCare] Advertencia: no se pudo conectar a la base de datos: {e}")
        return False


def create_tables_if_possible():
    """
    Intenta crear las tablas del sistema solo si la base de datos está disponible.
    Si la conexión falla, no detiene el arranque de la API.
    """
    try:
        if check_database_connection():
            Base.metadata.create_all(bind=engine)
            print("[ClinCare] Tablas verificadas/creadas correctamente.")
        else:
            print("[ClinCare] La API iniciará sin conexión activa a la base de datos.")
    except SQLAlchemyError as e:
        print(f"[ClinCare] No fue posible crear las tablas: {e}")