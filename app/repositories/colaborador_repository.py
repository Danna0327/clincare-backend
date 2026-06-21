from sqlalchemy.orm import Session
from app.models.colaborador import Colaborador

class ColaboradorRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Colaborador).all()

    def create(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj