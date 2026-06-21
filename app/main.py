from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
from app.controllers.paciente_controller import router as paciente_router

# Importar modelos para que SQLAlchemy los registre antes de create_all
from app.models.paciente import Paciente  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION
)

app.include_router(paciente_router)


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