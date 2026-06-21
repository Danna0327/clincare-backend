from app.controllers.cita_controller import router as cita_router
from app.controllers.colaborador_controller import router as colaborador_router
from app.controllers.paciente_controller import router as paciente_router

__all__ = ["paciente_router", "colaborador_router", "cita_router"]