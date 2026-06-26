import pytest
from unittest.mock import MagicMock
from app.services.paciente_service import PacienteService


def test_listar_pacientes():
    mock_db = MagicMock()
    service = PacienteService(mock_db)

    service.repository.get_all = MagicMock(return_value=["p1", "p2"])

    result = service.listar_pacientes()

    assert len(result) == 2