from app.repositories.colaborador_repository import ColaboradorRepository

class ColaboradorService:

    def __init__(self, repo: ColaboradorRepository):
        self.repo = repo

    def listar(self):
        return self.repo.get_all()

    def crear(self, data):
        if data.tipo_colaborador not in ["MEDICO", "ADMINISTRATIVO"]:
            raise ValueError("Tipo inválido")

        return self.repo.create(data)