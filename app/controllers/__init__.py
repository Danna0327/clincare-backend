from .paciente_controller import router as paciente_router
from .colaborador_controller import router as colaborador_router
from .cita_controller import router as cita_router

__all__ = [
    "paciente_router",
    "colaborador_router",
    "cita_router"
]