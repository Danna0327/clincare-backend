from app.repositories.usuario_repository import UsuarioRepository
from app.core.security import verify_password

class AuthService:

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def login(self, username: str, password: str):

        user = self.repo.get_by_username(username)

        if not user:
            raise Exception("Usuario no encontrado")

        if not verify_password(password, user.password_hash):
            raise Exception("Contraseña incorrecta")

        return {
            "message": "Login exitoso",
            "user": user.username
        }