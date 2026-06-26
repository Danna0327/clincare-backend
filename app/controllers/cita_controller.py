from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.cita_schema import (
    CitaCreate,
    CitaEstadoUpdate,
    CitaResponse,
    CitasPorCedulaResponse,
    CitaUpdate
)
from app.services.cita_service import CitaService

router = APIRouter(
    prefix="/citas",
    tags=["Citas"]
)


@router.get("/", response_model=List[CitaResponse])
def listar_citas(db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.listar_citas()


@router.get("/{cita_id}", response_model=CitaResponse)
def obtener_cita(cita_id: int, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.obtener_cita_por_id(cita_id)


@router.post("/", response_model=CitaResponse, status_code=status.HTTP_201_CREATED)
def crear_cita(data: CitaCreate, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.crear_cita(data)


@router.put("/{cita_id}", response_model=CitaResponse)
def actualizar_cita(cita_id: int, data: CitaUpdate, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.actualizar_cita(cita_id, data)


@router.patch("/{cita_id}/estado")
def cambiar_estado_cita(cita_id: int, data: CitaEstadoUpdate, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.cambiar_estado_cita(cita_id, data)


@router.get("/paciente/{cedula}", response_model=CitasPorCedulaResponse)
def obtener_citas_por_cedula(cedula: str, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.obtener_citas_por_cedula(cedula)


@router.delete("/{cita_id}")
def eliminar_cita(cita_id: int, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.eliminar_cita(cita_id)