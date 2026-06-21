from pydantic import BaseModel

class ColaboradorCreate(BaseModel):
    cedula: str
    nombres: str
    apellidos: str
    correo: str
    telefono: str | None = None
    tipo_colaborador: str
    especialidad: str | None = None

class ColaboradorResponse(ColaboradorCreate):
    id: int