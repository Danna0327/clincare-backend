from fastapi import FastAPI

from app.core.config import settings
from app.core.database import create_tables_if_possible
from app.controllers.paciente_controller import router as paciente_router

# Importar modelos para que SQLAlchemy los registre
from app.models.paciente import Paciente  # noqa: F401

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION
)


@app.on_event("startup")
def startup_event():
    """
    Evento de inicio de la aplicación.
    Intenta conectar a la base de datos y crear tablas si la conexión está disponible.
    Si la base no responde, la API sigue levantando para permitir continuar el desarrollo.
    """
    create_tables_if_possible()


@app.get("/", tags=["Health Check"])
def root():
    return {
        "message": "ClinCare API funcionando correctamente",
        "version": settings.APP_VERSION
    }


@app.get("/health", tags=["Health Check"])
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME
    }


app.include_router(paciente_router)