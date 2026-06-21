from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.paciente import Paciente
from app.schemas.paciente_schema import PacienteCreate, PacienteUpdate


class PacienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Paciente]:
        return self.db.query(Paciente).all()

    def get_by_id(self, paciente_id: int) -> Optional[Paciente]:
        return self.db.query(Paciente).filter(Paciente.id == paciente_id).first()

    def get_by_cedula(self, cedula: str) -> Optional[Paciente]:
        return self.db.query(Paciente).filter(Paciente.cedula == cedula).first()

    def get_by_correo(self, correo: str) -> Optional[Paciente]:
        return self.db.query(Paciente).filter(Paciente.correo == correo).first()

    def create(self, paciente_data: PacienteCreate) -> Paciente:
        nuevo_paciente = Paciente(**paciente_data.model_dump())
        self.db.add(nuevo_paciente)
        self.db.commit()
        self.db.refresh(nuevo_paciente)
        return nuevo_paciente

    def update(self, paciente: Paciente, paciente_data: PacienteUpdate) -> Paciente:
        update_data = paciente_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(paciente, key, value)

        self.db.commit()
        self.db.refresh(paciente)
        return paciente

    def delete(self, paciente: Paciente) -> None:
        self.db.delete(paciente)
        self.db.commit()