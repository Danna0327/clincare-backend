from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.db.database import create_tables_if_possible
from app.controllers.paciente_controller import router as paciente_router
from app.controllers.colaborador_controller import router as colaborador_router
from app.controllers.cita_controller import router as cita_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Evento de inicio de la aplicación.
    Intenta crear tablas si la BD está disponible, sin bloquear el arranque.
    """
    create_tables_if_possible()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    lifespan=lifespan
)


@app.get("/", tags=["Inicio"])
def root():
    return {
        "message": "ClinCare API funcionando correctamente",
        "version": settings.APP_VERSION
    }


@app.get("/health", tags=["Monitoreo"])
def health_check():
    return {
        "status": "ok",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


# Prefijo general de API
API_PREFIX = "/api/v1"

# Routers
app.include_router(paciente_router, prefix=API_PREFIX)
app.include_router(colaborador_router, prefix=API_PREFIX)
app.include_router(cita_router, prefix=API_PREFIX)