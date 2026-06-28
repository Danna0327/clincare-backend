from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.cita_schema import (
    CitaCreate,
    CitaResponse,
    CitaUpdate,
    CambioEstadoCita,
)
from app.services.cita_service import CitaService

router = APIRouter(
    prefix="/citas",
    tags=["Citas"],
)


@router.get(
    "/",
    response_model=List[CitaResponse],
    summary="Listar citas",
)
def listar_citas(
    db: Session = Depends(get_db),
):
    """
    Obtiene todas las citas registradas.
    """
    service = CitaService(db)
    return service.listar_citas()


@router.get(
    "/{cita_id}",
    response_model=CitaResponse,
    summary="Obtener cita por ID",
)
def obtener_cita(
    cita_id: int,
    db: Session = Depends(get_db),
):
    """
    Obtiene una cita mediante su identificador.
    """
    service = CitaService(db)
    return service.obtener_cita_por_id(cita_id)


@router.post(
    "/",
    response_model=CitaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar cita",
)
def crear_cita(
    data: CitaCreate,
    db: Session = Depends(get_db),
):
    """
    Registra una nueva cita médica.
    """
    service = CitaService(db)
    return service.crear_cita(data)


@router.put(
    "/{cita_id}",
    response_model=CitaResponse,
    summary="Actualizar cita",
)
def actualizar_cita(
    cita_id: int,
    data: CitaUpdate,
    db: Session = Depends(get_db),
):
    """
    Actualiza la información de una cita.
    """
    service = CitaService(db)
    return service.actualizar_cita(cita_id, data)


@router.patch(
    "/{cita_id}/estado",
    response_model=CitaResponse,
    summary="Cambiar estado de una cita",
)
def cambiar_estado(
    cita_id: int,
    data: CambioEstadoCita,
    db: Session = Depends(get_db),
):
    """
    Cambia el estado de una cita médica.
    """
    service = CitaService(db)
    return service.cambiar_estado(cita_id, data)


@router.get(
    "/paciente/{cedula}",
    response_model=List[CitaResponse],
    summary="Consultar citas por cédula",
)
def consultar_por_cedula(
    cedula: str,
    db: Session = Depends(get_db),
):
    """
    Consulta todas las citas asociadas a la cédula de un paciente.
    """
    service = CitaService(db)
    return service.consultar_por_cedula(cedula)


@router.delete(
    "/{cita_id}",
    summary="Eliminar cita",
)
def eliminar_cita(
    cita_id: int,
    db: Session = Depends(get_db),
):
    """
    Elimina una cita del sistema.
    """
    service = CitaService(db)
    return service.eliminar_cita(cita_id)