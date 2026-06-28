from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.paciente_schema import (
    PacienteCreate,
    PacienteResponse,
    PacienteUpdate,
)
from app.services.paciente_service import PacienteService

router = APIRouter(
    prefix="/pacientes",
    tags=["Pacientes"],
)


@router.get(
    "/",
    response_model=List[PacienteResponse],
    summary="Listar pacientes",
)
def listar_pacientes(
    db: Session = Depends(get_db),
):
    """
    Obtiene la lista completa de pacientes registrados.
    """
    service = PacienteService(db)
    return service.listar_pacientes()


@router.get(
    "/{paciente_id}",
    response_model=PacienteResponse,
    summary="Obtener paciente por ID",
)
def obtener_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
):
    """
    Obtiene un paciente mediante su identificador.
    """
    service = PacienteService(db)
    return service.obtener_paciente_por_id(paciente_id)


@router.post(
    "/",
    response_model=PacienteResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar paciente",
)
def crear_paciente(
    data: PacienteCreate,
    db: Session = Depends(get_db),
):
    """
    Registra un nuevo paciente.
    """
    service = PacienteService(db)
    return service.crear_paciente(data)


@router.put(
    "/{paciente_id}",
    response_model=PacienteResponse,
    summary="Actualizar paciente",
)
def actualizar_paciente(
    paciente_id: int,
    data: PacienteUpdate,
    db: Session = Depends(get_db),
):
    """
    Actualiza la información de un paciente existente.
    """
    service = PacienteService(db)
    return service.actualizar_paciente(paciente_id, data)


@router.delete(
    "/{paciente_id}",
    summary="Eliminar paciente",
)
def eliminar_paciente(
    paciente_id: int,
    db: Session = Depends(get_db),
):
    """
    Elimina un paciente del sistema.
    """
    service = PacienteService(db)
    return service.eliminar_paciente(paciente_id)