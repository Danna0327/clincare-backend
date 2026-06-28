from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.core.database import Base


class Colaborador(Base):
    """
    Modelo de colaboradores del sistema.
    Puede representar médicos o personal administrativo.
    """

    __tablename__ = "colaboradores"

    id = Column(Integer, primary_key=True, index=True)

    cedula = Column(String(10), unique=True, nullable=False, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(15), nullable=False)

    rol = Column(String(20), nullable=False)
    especialidad = Column(String(100), nullable=True)

    activo = Column(Boolean, default=True, nullable=False)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
