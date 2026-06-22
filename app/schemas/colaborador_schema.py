from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class ColaboradorBase(BaseModel):
    cedula: str = Field(..., min_length=10, max_length=10)
    nombres: str = Field(..., min_length=2, max_length=100)
    apellidos: str = Field(..., min_length=2, max_length=100)
    correo: EmailStr
    telefono: str = Field(..., min_length=7, max_length=15)
    rol: str = Field(..., description="MEDICO o ADMINISTRATIVO")
    especialidad: Optional[str] = Field(default=None, max_length=100)
    activo: bool = True

    @field_validator("rol")
    @classmethod
    def validar_rol(cls, value: str) -> str:
        value = value.upper().strip()
        if value not in ["MEDICO", "ADMINISTRATIVO"]:
            raise ValueError("El rol debe ser MEDICO o ADMINISTRATIVO")
        return value

    @field_validator("especialidad")
    @classmethod
    def limpiar_especialidad(cls, value):
        if value is None:
            return None
        return value.strip()


class ColaboradorCreate(ColaboradorBase):
    pass


class ColaboradorUpdate(BaseModel):
    nombres: Optional[str] = Field(default=None, min_length=2, max_length=100)
    apellidos: Optional[str] = Field(default=None, min_length=2, max_length=100)
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = Field(default=None, min_length=7, max_length=15)
    rol: Optional[str] = None
    especialidad: Optional[str] = Field(default=None, max_length=100)
    activo: Optional[bool] = None

    @field_validator("rol")
    @classmethod
    def validar_rol(cls, value):
        if value is None:
            return value
        value = value.upper().strip()
        if value not in ["MEDICO", "ADMINISTRATIVO"]:
            raise ValueError("El rol debe ser MEDICO o ADMINISTRATIVO")
        return value


class ColaboradorResponse(ColaboradorBase):
    id: int

    model_config = ConfigDict(from_attributes=True)