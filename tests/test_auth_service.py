from types import SimpleNamespace

import pytest

from app.services.auth_service import AuthService


class DummyRepo:
    def __init__(self, usuario=None):
        self.usuario = usuario
        self.calls = []

    def get_by_username(self, username):
        self.calls.append(username)
        return self.usuario


def test_login_ok(monkeypatch):
    usuario = SimpleNamespace(username="admin", estado="ACTIVO", password_hash="hash", rol="ADMIN")
    repo = DummyRepo(usuario)
    service = AuthService(repo)

    monkeypatch.setattr("app.services.auth_service.verify_password", lambda password, stored: True)
    monkeypatch.setattr("app.services.auth_service.create_access_token", lambda payload: "token")

    result = service.login(SimpleNamespace(username="admin", password="123456"))

    assert result.access_token == "token"
    assert result.token_type == "bearer"


def test_login_user_not_found():
    repo = DummyRepo(None)
    service = AuthService(repo)

    with pytest.raises(ValueError, match="Usuario o contraseña incorrectos"):
        service.login(SimpleNamespace(username="admin", password="123456"))


def test_login_inactive_user():
    usuario = SimpleNamespace(username="admin", estado="INACTIVO", password_hash="hash", rol="ADMIN")
    repo = DummyRepo(usuario)
    service = AuthService(repo)

    with pytest.raises(ValueError, match="Usuario inactivo"):
        service.login(SimpleNamespace(username="admin", password="123456"))


def test_login_wrong_password(monkeypatch):
    usuario = SimpleNamespace(username="admin", estado="ACTIVO", password_hash="hash", rol="ADMIN")
    repo = DummyRepo(usuario)
    service = AuthService(repo)

    monkeypatch.setattr("app.services.auth_service.verify_password", lambda password, stored: False)

    with pytest.raises(ValueError, match="Credenciales incorrectas"):
        service.login(SimpleNamespace(username="admin", password="123456"))
