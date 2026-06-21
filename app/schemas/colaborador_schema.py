from pydantic import BaseModel

class ColaboradorCreate(BaseModel):
    cedula: str
    nombres: str
    apellidos: str
    correo: str
    tipo: str