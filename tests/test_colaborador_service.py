import pytest
from unittest.mock import MagicMock

from app.services.colaborador_service import ColaboradorService


def test_listar_colaboradores():
    """
    Verifica que el servicio consulte correctamente
    el repositorio de colaboradores.
    """

    mock_db = MagicMock()
    service = ColaboradorService(mock_db)

    service.repository.get_all = MagicMock(return_value=["c1"])

    resultado = service.listar_colaboradores()

    service.repository.get_all.assert_called_once()

    assert len(resultado) == 1
    assert resultado == ["c1"]