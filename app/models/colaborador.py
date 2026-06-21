from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Colaborador(Base):
    __tablename__ = "colaboradores"

    id = Column(Integer, primary_key=True)
    cedula = Column(String(10), unique=True)
    nombres = Column(String(100))
    apellidos = Column(String(100))
    correo = Column(String(100))
    tipo = Column(String(30))
    estado = Column(String(20), default="ACTIVO")
    created_at = Column(DateTime, server_default=func.now())