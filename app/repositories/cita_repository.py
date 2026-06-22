from typing import Optional

from sqlalchemy.orm import Session, joinedload

from app.models.cita import Cita
from app.schemas.cita_schema import CitaCreate, CitaUpdate


class CitaRepository:
    """
    Responsable únicamente de la persistencia de citas.
    SOLID:
    - S: solo acceso a datos de Cita
    """

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Cita).order_by(Cita.id.asc()).all()

    def get_by_id(self, cita_id: int) -> Optional[Cita]:
        return self.db.query(Cita).filter(Cita.id == cita_id).first()

    def create(self, cita_data: CitaCreate) -> Cita:
        cita = Cita(**cita_data.model_dump())
        self.db.add(cita)
        self.db.commit()
        self.db.refresh(cita)
        return cita

    def update(self, cita: Cita, cita_data: CitaUpdate) -> Cita:
        update_data = cita_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(cita, field, value)

        self.db.commit()
        self.db.refresh(cita)
        return cita

    def delete(self, cita: Cita) -> None:
        self.db.delete(cita)
        self.db.commit()

    def get_by_paciente_id(self, paciente_id: int):
        return (
            self.db.query(Cita)
            .options(joinedload(Cita.medico), joinedload(Cita.paciente))
            .filter(Cita.paciente_id == paciente_id)
            .order_by(Cita.fecha.asc(), Cita.hora.asc())
            .all()
        )