from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.paciente_repository import PacienteRepository
from app.schemas.paciente_schema import (
    PacienteCreate,
    PacienteUpdate,
    PacienteResponse
)
from app.services.paciente_service import PacienteService

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])


def get_paciente_service(db: Session = Depends(get_db)) -> PacienteService:
    repository = PacienteRepository(db)
    return PacienteService(repository)


@router.get("/", response_model=List[PacienteResponse], status_code=status.HTTP_200_OK)
def listar_pacientes(service: PacienteService = Depends(get_paciente_service)):
    return service.listar_pacientes()


@router.get("/{paciente_id}", response_model=PacienteResponse, status_code=status.HTTP_200_OK)
def obtener_paciente(paciente_id: int, service: PacienteService = Depends(get_paciente_service)):
    return service.obtener_paciente_por_id(paciente_id)


@router.post("/", response_model=PacienteResponse, status_code=status.HTTP_201_CREATED)
def crear_paciente(
    paciente_data: PacienteCreate,
    service: PacienteService = Depends(get_paciente_service)
):
    return service.crear_paciente(paciente_data)


@router.put("/{paciente_id}", response_model=PacienteResponse, status_code=status.HTTP_200_OK)
def actualizar_paciente(
    paciente_id: int,
    paciente_data: PacienteUpdate,
    service: PacienteService = Depends(get_paciente_service)
):
    return service.actualizar_paciente(paciente_id, paciente_data)


@router.delete("/{paciente_id}", status_code=status.HTTP_200_OK)
def eliminar_paciente(
    paciente_id: int,
    service: PacienteService = Depends(get_paciente_service)
):
    return service.eliminar_paciente(paciente_id)