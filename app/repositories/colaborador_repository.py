from typing import Optional
from sqlalchemy.orm import Session
from app.models.colaborador import Colaborador
from app.schemas.colaborador_schema import ColaboradorCreate, ColaboradorUpdate


from sqlalchemy.orm import Session

from app.models.colaborador import Colaborador
from app.schemas.colaborador_schema import ColaboradorCreate, ColaboradorUpdate


class ColaboradorRepository:
    """
    Responsable solo de la persistencia de Colaborador.
    SOLID:
    - S: una única responsabilidad -> acceso a datos
    """

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Colaborador).order_by(Colaborador.id.asc()).all()

    def get_by_id(self, colaborador_id: int) -> Optional[Colaborador]:
        return self.db.query(Colaborador).filter(Colaborador.id == colaborador_id).first()

    def get_by_cedula(self, cedula: str) -> Optional[Colaborador]:
        return self.db.query(Colaborador).filter(Colaborador.cedula == cedula).first()

    def get_by_correo(self, correo: str) -> Optional[Colaborador]:
        return self.db.query(Colaborador).filter(Colaborador.correo == correo).first()

    def get_medicos(self):
        return (
            self.db.query(Colaborador)
            .filter(Colaborador.rol == "MEDICO")
            .order_by(Colaborador.id.asc())
            .all()
        )

    def get_administrativos(self):
        return (
            self.db.query(Colaborador)
            .filter(Colaborador.rol == "ADMINISTRATIVO")
            .order_by(Colaborador.id.asc())
            .all()
        )

    def create(self, colaborador_data: ColaboradorCreate) -> Colaborador:
        colaborador = Colaborador(**colaborador_data.model_dump())
        self.db.add(colaborador)
        self.db.commit()
        self.db.refresh(colaborador)
        return colaborador

    def update(self, colaborador: Colaborador, colaborador_data: ColaboradorUpdate) -> Colaborador:
        update_data = colaborador_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(colaborador, field, value)

        for field, value in update_data.items():
            setattr(colaborador, field, value)

        self.db.commit()
        self.db.refresh(colaborador)
        return colaborador

    def delete(self, colaborador: Colaborador) -> None:
        self.db.delete(colaborador)
        self.db.commit()