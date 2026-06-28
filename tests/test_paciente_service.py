import pytest
from unittest.mock import MagicMock

from app.services.paciente_service import PacienteService


def test_listar_pacientes():
    """
    Verifica que el servicio devuelva la lista de pacientes
    proporcionada por el repositorio.
    """

    mock_db = MagicMock()
    service = PacienteService(mock_db)

    service.repository.get_all = MagicMock(return_value=["p1", "p2"])

    resultado = service.listar_pacientes()

    service.repository.get_all.assert_called_once()

    assert len(resultado) == 2
    assert resultado == ["p1", "p2"]