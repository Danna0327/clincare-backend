from app.schemas.colaborador_schema import (
    ColaboradorBase,
    ColaboradorCreate,
    ColaboradorResponse,
    ColaboradorUpdate,
)
from app.schemas.paciente_schema import (
    PacienteBase,
    PacienteCreate,
    PacienteResponse,
    PacienteUpdate,
)

__all__ = [
    "PacienteBase",
    "PacienteCreate",
    "PacienteResponse",
    "PacienteUpdate",
    "ColaboradorBase",
    "ColaboradorCreate",
    "ColaboradorResponse",
    "ColaboradorUpdate",
]