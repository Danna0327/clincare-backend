from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class PacienteBase(BaseModel):
    cedula: str = Field(..., min_length=10, max_length=10, description="Cédula del paciente")
    nombres: str = Field(..., min_length=2, max_length=100)
    apellidos: str = Field(..., min_length=2, max_length=100)
    correo: EmailStr
    telefono: str = Field(..., min_length=7, max_length=15)
    direccion: Optional[str] = Field(default=None, max_length=255)
    fecha_nacimiento: Optional[str] = Field(default=None, max_length=20)
    activo: bool = True


class PacienteCreate(PacienteBase):
    pass


class PacienteUpdate(BaseModel):
    nombres: Optional[str] = Field(default=None, min_length=2, max_length=100)
    apellidos: Optional[str] = Field(default=None, min_length=2, max_length=100)
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = Field(default=None, min_length=7, max_length=15)
    direccion: Optional[str] = Field(default=None, max_length=255)
    fecha_nacimiento: Optional[str] = Field(default=None, max_length=20)
    activo: Optional[bool] = None


class PacienteResponse(PacienteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)