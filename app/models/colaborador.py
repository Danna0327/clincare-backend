
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.core.database import Base



class Colaborador(Base):
    __tablename__ = "colaboradores"

    id = Column(Integer, primary_key=True, index=True)

    cedula = Column(String(10), unique=True, nullable=False)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20))
    tipo_colaborador = Column(String(20), nullable=False)
    especialidad = Column(String(100))
    estado = Column(String(20), default="ACTIVO")
    created_at = Column(DateTime, server_default=func.now())

    cedula = Column(String(10), unique=True, nullable=False, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(15), nullable=False)
    rol = Column(String(20), nullable=False)  # MEDICO / ADMINISTRATIVO
    especialidad = Column(String(100), nullable=True)  # solo si es médico
    activo = Column(Boolean, default=True, nullable=False)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
