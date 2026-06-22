from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.cita_schema import (
    CitaCreate,
    CitaEstadoUpdate,
    CitaResponse,
    CitaUpdate
)
from app.services.cita_service import CitaService

router = APIRouter(
    prefix="/api/citas",
    tags=["Citas"]
)


@router.get("/", response_model=list[CitaResponse], status_code=status.HTTP_200_OK)
def listar_citas(db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.listar_citas()


@router.get("/{cita_id}", response_model=CitaResponse, status_code=status.HTTP_200_OK)
def obtener_cita(cita_id: int, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.obtener_cita_por_id(cita_id)


@router.post("/", response_model=CitaResponse, status_code=status.HTTP_201_CREATED)
def crear_cita(cita_data: CitaCreate, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.crear_cita(cita_data)


@router.put("/{cita_id}", response_model=CitaResponse, status_code=status.HTTP_200_OK)
def actualizar_cita(
    cita_id: int,
    cita_data: CitaUpdate,
    db: Session = Depends(get_db)
):
    service = CitaService(db)
    return service.actualizar_cita(cita_id, cita_data)


@router.patch("/{cita_id}/estado", response_model=CitaResponse, status_code=status.HTTP_200_OK)
def cambiar_estado_cita(
    cita_id: int,
    estado_data: CitaEstadoUpdate,
    db: Session = Depends(get_db)
):
    service = CitaService(db)
    return service.cambiar_estado_cita(cita_id, estado_data)


@router.delete("/{cita_id}", status_code=status.HTTP_200_OK)
def eliminar_cita(cita_id: int, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.eliminar_cita(cita_id)