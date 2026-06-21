from fastapi import FastAPI

from app.controllers.cita_controller import router as cita_router
from app.controllers.colaborador_controller import router as colaborador_router
from app.controllers.paciente_controller import router as paciente_router
from app.core.config import settings
from app.core.database import create_tables_if_possible

# Importar modelos para registrar metadata
from app.models.cita import Cita  # noqa: F401
from app.models.colaborador import Colaborador  # noqa: F401
from app.models.paciente import Paciente  # noqa: F401

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION
)


@app.on_event("startup")
def startup_event():
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
app.include_router(colaborador_router)
app.include_router(cita_router)