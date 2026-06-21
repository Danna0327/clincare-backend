from app.models.colaborador import Colaborador

class ColaboradorRepository:

    def __init__(self, db):
        self.db = db

    def create(self, data):
        obj = Colaborador(**data.dict())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_all(self):
        return self.db.query(Colaborador).all()