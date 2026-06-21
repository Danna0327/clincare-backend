from app.models.colaborador import Colaborador

class ColaboradorService:

    def __init__(self, repo):
        self.repo = repo

    def crear(self, data):

        nuevo = Colaborador(**data.dict())
        return self.repo.create(nuevo)