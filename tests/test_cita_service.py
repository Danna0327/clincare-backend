import pytest
from unittest.mock import MagicMock
from app.services.cita_service import CitaService


def test_listar_citas():
    mock_db = MagicMock()
    service = CitaService(mock_db)

    service.repository.get_all = MagicMock(return_value=["cita1", "cita2"])

    result = service.listar_citas()

    assert len(result) == 2