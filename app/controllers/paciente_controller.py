from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.paciente_schema import (
    PacienteCreate,
    PacienteResponse,
    PacienteUpdate
)
from app.services.paciente_service import PacienteService

router = APIRouter(
    prefix="/pacientes",
    tags=["Pacientes"]
)


@router.get("/", response_model=List[PacienteResponse], summary="Listar pacientes")
def listar_pacientes(db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.obtener_todos()


@router.get("/{paciente_id}", response_model=PacienteResponse, summary="Obtener paciente por ID")
def obtener_paciente(paciente_id: int, db: Session = Depends(get_db)):
    service = PacienteService(db)
    paciente = service.obtener_por_id(paciente_id)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente no encontrado"
        )
    return paciente


@router.post("/", response_model=PacienteResponse, status_code=status.HTTP_201_CREATED, summary="Registrar paciente")
def crear_paciente(data: PacienteCreate, db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.crear(data)


@router.put("/{paciente_id}", response_model=PacienteResponse, summary="Actualizar paciente")
def actualizar_paciente(paciente_id: int, data: PacienteUpdate, db: Session = Depends(get_db)):
    service = PacienteService(db)
    paciente = service.actualizar(paciente_id, data)
    if not paciente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente no encontrado"
        )
    return paciente


@router.delete("/{paciente_id}", status_code=status.HTTP_200_OK, summary="Eliminar paciente")
def eliminar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    service = PacienteService(db)
    eliminado = service.eliminar(paciente_id)
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente no encontrado"
        )
    return {"message": "Paciente eliminado correctamente"}