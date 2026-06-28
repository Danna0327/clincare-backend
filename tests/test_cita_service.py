from types import SimpleNamespace

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


def test_cambiar_estado_cita():
    mock_db = MagicMock()
    service = CitaService(mock_db)

    cita = SimpleNamespace(estado="PENDIENTE")
    service.repository.get_by_id = MagicMock(return_value=cita)

    resultado = service.cambiar_estado_cita(1, SimpleNamespace(estado="ATENDIDA"))

    assert resultado.estado == "ATENDIDA"
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(cita)


def test_obtener_citas_por_cedula():
    mock_db = MagicMock()
    service = CitaService(mock_db)

    paciente = SimpleNamespace(id=7, cedula="1234567890", nombres="Ana", apellidos="Lopez")
    mock_db.query.return_value.filter.return_value.first.return_value = paciente
    service.repository.get_by_paciente_id = MagicMock(return_value=[])

    resultado = service.obtener_citas_por_cedula("1234567890")

    assert resultado.paciente_id == 7
    assert resultado.total_citas == 0