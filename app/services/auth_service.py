#COMMIT 13 — auth service

from app.repositories.usuario_repository import UsuarioRepository
from app.core.security import verify_password, create_token

class AuthService:
    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def login(self, username, password):
        user = self.repo.get_by_username(username)

        if not user:
            raise Exception("Usuario no existe")

        if not verify_password(password, user.password_hash):
            raise Exception("Credenciales incorrectas")

        return create_token({"sub": user.username, "rol": user.rol})