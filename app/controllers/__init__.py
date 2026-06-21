from app.controllers.auth_controller import router as auth_router
from app.controllers.colaborador_controller import router as colaborador_router
from app.controllers.paciente_controller import router as paciente_router
from app.controllers.cita_controller import router as cita_router

__all__ = [
    "auth_router",
    "colaborador_router",
    "paciente_router",
    "cita_router"
]