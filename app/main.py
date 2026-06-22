from fastapi import FastAPI

from app.controllers.paciente_controller import router as paciente_router
from app.controllers.colaborador_controller import router as colaborador_router
from app.controllers.cita_controller import router as cita_router

from app.core.config import settings
from app.core.database import Base, engine

# Importar modelos para que SQLAlchemy los registre
from app.models.paciente import Paciente
from app.models.colaborador import Colaborador
from app.models.cita import Cita
from app.models.usuario import Usuario


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION
)


@app.on_event("startup")
def startup_event():
    """
    Intenta crear tablas al iniciar.
    Si SQL Server no está disponible, la API sigue levantando.
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("[ClinCare] Base de datos conectada y tablas verificadas correctamente.")
    except Exception as e:
        print(f"[ClinCare] Advertencia: no se pudo conectar a la base de datos: {e}")
        print("[ClinCare] La API iniciará sin conexión activa a la base de datos.")


@app.get("/")
def root():
    return {
        "message": "ClinCare API funcionando correctamente",
        "version": settings.APP_VERSION
    }


# Routers
app.include_router(paciente_router, prefix="/api/v1", tags=["Pacientes"])
app.include_router(colaborador_router, prefix="/api/v1", tags=["Colaboradores"])
app.include_router(cita_router, prefix="/api/v1", tags=["Citas"])