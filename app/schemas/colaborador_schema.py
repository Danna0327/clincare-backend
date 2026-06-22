from typing import Optional
from pydantic import BaseModel, EmailStr

class ColaboradorBase(BaseModel):
    cedula: str
    nombres: str
    apellidos: str
    correo: EmailStr
    telefono: Optional[str] = None
    tipo_colaborador: str
    especialidad: Optional[str] = None
    estado: str = "ACTIVO"

class ColaboradorCreate(ColaboradorBase):
    pass

class ColaboradorUpdate(BaseModel):
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    tipo_colaborador: Optional[str] = None
    especialidad: Optional[str] = None
    estado: Optional[str] = None

class ColaboradorResponse(ColaboradorBase):
    id: int

    class Config:
        from_attributes = True