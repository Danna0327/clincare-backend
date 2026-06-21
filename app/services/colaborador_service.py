class ColaboradorService:

    def __init__(self, repo):
        self.repo = repo

    def crear(self, data):
        return self.repo.create(data)

    def listar(self):
        return self.repo.get_all()