from datetime import date, time
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

# Estados permitidos para una cita
ESTADOS_VALIDOS = {
    "PENDIENTE",
    "ATENDIDA",
    "CANCELADA"
}

# Estados permitidos para el cambio manual de estado
ESTADOS_TRANSICION_MANUAL = {
    "ATENDIDA",
    "CANCELADA"
}


class CitaBase(BaseModel):
    """
    Información base de una cita médica.
    """

    paciente_id: int = Field(..., gt=0)
    medico_id: int = Field(..., gt=0)
    fecha: date
    hora: time
    motivo: str = Field(..., min_length=5, max_length=255)
    estado: str = Field(default="PENDIENTE")

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, value: str):
        value = value.upper().strip()

        if value not in ESTADOS_VALIDOS:
            raise ValueError(
                "El estado debe ser PENDIENTE, ATENDIDA o CANCELADA"
            )

        return value


class CitaCreate(CitaBase):
    """Esquema para crear citas."""
    pass


class CitaUpdate(BaseModel):
    """Esquema para actualizar citas."""

    paciente_id: Optional[int] = Field(default=None, gt=0)
    medico_id: Optional[int] = Field(default=None, gt=0)
    fecha: Optional[date] = None
    hora: Optional[time] = None
    motivo: Optional[str] = Field(default=None, min_length=5, max_length=255)
    estado: Optional[str] = None

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, value):

        if value is None:
            return value

        value = value.upper().strip()

        if value not in ESTADOS_VALIDOS:
            raise ValueError(
                "El estado debe ser PENDIENTE, ATENDIDA o CANCELADA"
            )

        return value


class CitaEstadoUpdate(BaseModel):
    """
    Esquema para cambiar únicamente el estado de una cita.
    """

    estado: str = Field(...)

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, value):

        value = value.upper().strip()

        if value not in ESTADOS_TRANSICION_MANUAL:
            raise ValueError(
                "Solo se permite cambiar el estado a ATENDIDA o CANCELADA"
            )

        return value


class CitaResponse(CitaBase):
    """
    Respuesta enviada por la API.
    """

    id: int

    model_config = ConfigDict(from_attributes=True)


class CitaConsultaItem(BaseModel):
    """
    Información resumida de una cita.
    """

    id: int
    fecha: date
    hora: time
    motivo: str
    estado: str
    medico_id: int
    medico_nombre: str

    model_config = ConfigDict(from_attributes=True)


class CitasPorCedulaResponse(BaseModel):
    """
    Respuesta para la consulta de citas por cédula.
    """

    paciente_id: int
    cedula: str
    paciente_nombre: str
    total_citas: int
    citas: list[CitaConsultaItem]