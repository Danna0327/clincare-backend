from datetime import date, time
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


ESTADOS_VALIDOS = {"PENDIENTE", "ATENDIDA", "CANCELADA"}
ESTADOS_TRANSICION_MANUAL = {"ATENDIDA", "CANCELADA"}


class CitaBase(BaseModel):
    paciente_id: int = Field(..., gt=0)
    medico_id: int = Field(..., gt=0)
    fecha: date
    hora: time
    motivo: str = Field(..., min_length=5, max_length=255)
    estado: str = Field(default="PENDIENTE")

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, value: str) -> str:
        value = value.upper().strip()
        if value not in ESTADOS_VALIDOS:
            raise ValueError("El estado debe ser PENDIENTE, ATENDIDA o CANCELADA")
        return value


class CitaCreate(CitaBase):
    pass


class CitaUpdate(BaseModel):
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
            raise ValueError("El estado debe ser PENDIENTE, ATENDIDA o CANCELADA")
        return value


class CitaEstadoUpdate(BaseModel):
    estado: str = Field(..., description="Nuevo estado de la cita")

    @field_validator("estado")
    @classmethod
    def validar_estado(cls, value: str) -> str:
        value = value.upper().strip()
        if value not in ESTADOS_TRANSICION_MANUAL:
            raise ValueError("Solo se permite cambiar el estado a ATENDIDA o CANCELADA")
        return value


class CitaResponse(CitaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)