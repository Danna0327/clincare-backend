import pytest
from unittest.mock import MagicMock
from app.services.colaborador_service import ColaboradorService


def test_listar_colaboradores():
    mock_db = MagicMock()
    service = ColaboradorService(mock_db)

    service.repository.get_all = MagicMock(return_value=["c1"])

    result = service.listar_colaboradores()

    assert len(result) == 1