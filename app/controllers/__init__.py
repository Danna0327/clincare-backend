from .auth_controller import router as auth_router
from .cita_controller import router as cita_router
from .colaborador_controller import router as colaborador_router
from .paciente_controller import router as paciente_router

__all__ = [
    "auth_router",
    "cita_router",
    "colaborador_router",
    "paciente_router",
]