import pytest
from unittest.mock import MagicMock

from app.services.cita_service import CitaService


def test_listar_citas():
    """
    Verifica que el servicio obtenga correctamente
    las citas almacenadas.
    """

    mock_db = MagicMock()
    service = CitaService(mock_db)

    service.repository.get_all = MagicMock(return_value=["cita1", "cita2"])

    resultado = service.listar_citas()

    service.repository.get_all.assert_called_once()

    assert len(resultado) == 2
    assert resultado == ["cita1", "cita2"]