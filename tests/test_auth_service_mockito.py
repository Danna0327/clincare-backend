from types import SimpleNamespace

from mockito import mock, unstub, when

import app.services.auth_service as auth_service_module
from app.schemas.auth_schema import LoginRequest
from app.services.auth_service import AuthService


def test_login_con_mockito():
    repo = mock()
    usuario = SimpleNamespace(
        username="admin",
        estado="ACTIVO",
        password_hash="hash123",
        rol="ADMIN",
    )

    when(repo).get_by_username("admin").thenReturn(usuario)
    when(auth_service_module).verify_password("secreto123", "hash123").thenReturn(True)
    when(auth_service_module).create_access_token({"sub": "admin", "rol": "ADMIN"}).thenReturn(
        "token-mockito"
    )

    try:
        service = AuthService(repo)
        resultado = service.login(
            LoginRequest(username="admin", password="secreto123")
        )

        assert resultado.access_token == "token-mockito"
        assert resultado.token_type == "bearer"
    finally:
        unstub()
