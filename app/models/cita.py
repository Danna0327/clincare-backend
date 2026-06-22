from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Time
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)

    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    medico_id = Column(Integer, ForeignKey("colaboradores.id"), nullable=False)

    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    motivo = Column(String(255), nullable=False)
    estado = Column(String(20), nullable=False, default="PENDIENTE")

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())

    paciente = relationship("Paciente")
    medico = relationship("Colaborador")