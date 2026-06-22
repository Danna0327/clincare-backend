from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.cita_schema import (
    CitaCreate,
    CitaEstadoUpdate,
    CitaResponse,
    CitaUpdate
)
from app.services.cita_service import CitaService

router = APIRouter(
    prefix="/citas",
    tags=["Citas"]
)


@router.get("/", response_model=List[CitaResponse], summary="Listar citas")
def listar_citas(db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.obtener_todas()


@router.get("/{cita_id}", response_model=CitaResponse, summary="Obtener cita por ID")
def obtener_cita(cita_id: int, db: Session = Depends(get_db)):
    service = CitaService(db)
    cita = service.obtener_por_id(cita_id)
    if not cita:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cita no encontrada"
        )
    return cita


@router.post("/", response_model=CitaResponse, status_code=status.HTTP_201_CREATED, summary="Registrar cita")
def crear_cita(data: CitaCreate, db: Session = Depends(get_db)):
    service = CitaService(db)
    return service.crear(data)


@router.put("/{cita_id}", response_model=CitaResponse, summary="Actualizar cita")
def actualizar_cita(cita_id: int, data: CitaUpdate, db: Session = Depends(get_db)):
    service = CitaService(db)
    cita = service.actualizar(cita_id, data)
    if not cita:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cita no encontrada"
        )
    return cita


@router.patch("/{cita_id}/estado", response_model=CitaResponse, summary="Cambiar estado de cita")
def cambiar_estado_cita(cita_id: int, data: CitaEstadoUpdate, db: Session = Depends(get_db)):
    service = CitaService(db)
    cita = service.cambiar_estado(cita_id, data.estado)
    if not cita:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cita no encontrada"
        )
    return cita


@router.delete("/{cita_id}", status_code=status.HTTP_200_OK, summary="Eliminar cita")
def eliminar_cita(cita_id: int, db: Session = Depends(get_db)):
    service = CitaService(db)
    eliminado = service.eliminar(cita_id)
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cita no encontrada"
        )
    return {"message": "Cita eliminada correctamente"}