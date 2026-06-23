from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.auth_schema import LoginRequest, TokenResponse
from app.core.security import verify_password, create_access_token

class AuthService:

    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    def login(self, data: LoginRequest) -> TokenResponse:
        usuario = self.usuario_repository.get_by_username(data.username)

        if not usuario:
            raise ValueError("Usuario o contraseña incorrectos")

        if usuario.estado != "ACTIVO":
            raise ValueError("Usuario inactivo")

        if not verify_password(data.password, usuario.password_hash):
            raise ValueError("Credenciales incorrectas")

        token = create_access_token({
            "sub": usuario.username,
            "rol": usuario.rol
        })

        return TokenResponse(access_token=token)