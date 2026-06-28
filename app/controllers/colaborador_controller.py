from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.colaborador_schema import (
    ColaboradorCreate,
    ColaboradorResponse,
    ColaboradorUpdate,
)
from app.services.colaborador_service import ColaboradorService

router = APIRouter(
    prefix="/colaboradores",
    tags=["Colaboradores"],
)


@router.get(
    "/",
    response_model=List[ColaboradorResponse],
    summary="Listar colaboradores",
)
def listar_colaboradores(
    db: Session = Depends(get_db),
):
    """
    Obtiene todos los colaboradores registrados.
    """
    service = ColaboradorService(db)
    return service.listar_colaboradores()


@router.get(
    "/{colaborador_id}",
    response_model=ColaboradorResponse,
    summary="Obtener colaborador por ID",
)
def obtener_colaborador(
    colaborador_id: int,
    db: Session = Depends(get_db),
):
    """
    Obtiene un colaborador mediante su identificador.
    """
    service = ColaboradorService(db)
    return service.obtener_colaborador_por_id(colaborador_id)


@router.post(
    "/",
    response_model=ColaboradorResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar colaborador",
)
def crear_colaborador(
    data: ColaboradorCreate,
    db: Session = Depends(get_db),
):
    """
    Registra un nuevo colaborador.
    """
    service = ColaboradorService(db)
    return service.crear_colaborador(data)


@router.put(
    "/{colaborador_id}",
    response_model=ColaboradorResponse,
    summary="Actualizar colaborador",
)
def actualizar_colaborador(
    colaborador_id: int,
    data: ColaboradorUpdate,
    db: Session = Depends(get_db),
):
    """
    Actualiza la información de un colaborador.
    """
    service = ColaboradorService(db)
    return service.actualizar_colaborador(colaborador_id, data)


@router.delete(
    "/{colaborador_id}",
    summary="Eliminar colaborador",
)
def eliminar_colaborador(
    colaborador_id: int,
    db: Session = Depends(get_db),
):
    """
    Elimina un colaborador del sistema.
    """
    service = ColaboradorService(db)
    return service.eliminar_colaborador(colaborador_id)

