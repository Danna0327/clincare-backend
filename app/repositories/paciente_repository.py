from typing import Optional

from sqlalchemy.orm import Session

from app.models.paciente import Paciente
from app.schemas.paciente_schema import PacienteCreate, PacienteUpdate


class PacienteRepository:
    """
    Repositorio responsable únicamente del acceso a datos de pacientes.
    Principio SOLID aplicado:
    - S (Single Responsibility): solo maneja persistencia/consulta de Paciente.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Paciente).order_by(Paciente.id.asc()).all()

    def get_by_id(self, paciente_id: int) -> Optional[Paciente]:
        return self.db.query(Paciente).filter(Paciente.id == paciente_id).first()

    def get_by_cedula(self, cedula: str) -> Optional[Paciente]:
        return self.db.query(Paciente).filter(Paciente.cedula == cedula).first()

    def get_by_correo(self, correo: str) -> Optional[Paciente]:
        return self.db.query(Paciente).filter(Paciente.correo == correo).first()

    def create(self, paciente_data: PacienteCreate) -> Paciente:
        paciente = Paciente(**paciente_data.model_dump())
        self.db.add(paciente)
        self.db.commit()
        self.db.refresh(paciente)
        return paciente

    def update(self, paciente: Paciente, paciente_data: PacienteUpdate) -> Paciente:
        update_data = paciente_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(paciente, field, value)

        self.db.commit()
        self.db.refresh(paciente)
        return paciente

    def delete(self, paciente: Paciente) -> None:
        self.db.delete(paciente)
        self.db.commit()