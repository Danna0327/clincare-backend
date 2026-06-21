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
    prefix="/api/pacientes",
    tags=["Pacientes"]
)


@router.get("/", response_model=list[PacienteResponse], status_code=status.HTTP_200_OK)
def listar_pacientes(db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.listar_pacientes()


@router.get("/{paciente_id}", response_model=PacienteResponse, status_code=status.HTTP_200_OK)
def obtener_paciente(paciente_id: int, db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.obtener_paciente_por_id(paciente_id)


@router.post("/", response_model=PacienteResponse, status_code=status.HTTP_201_CREATED)
def crear_paciente(paciente_data: PacienteCreate, db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.crear_paciente(paciente_data)


@router.put("/{paciente_id}", response_model=PacienteResponse, status_code=status.HTTP_200_OK)
def actualizar_paciente(
    paciente_id: int,
    paciente_data: PacienteUpdate,
    db: Session = Depends(get_db)
):
    service = PacienteService(db)
    return service.actualizar_paciente(paciente_id, paciente_data)


@router.delete("/{paciente_id}", status_code=status.HTTP_200_OK)
def eliminar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.eliminar_paciente(paciente_id)