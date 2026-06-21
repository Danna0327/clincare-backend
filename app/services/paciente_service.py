from typing import List

from fastapi import HTTPException, status

from app.repositories.paciente_repository import PacienteRepository
from app.schemas.paciente_schema import (
    PacienteCreate,
    PacienteUpdate,
    PacienteResponse
)


class PacienteService:
    def __init__(self, repository: PacienteRepository):
        self.repository = repository

    def listar_pacientes(self) -> List[PacienteResponse]:
        pacientes = self.repository.get_all()
        return [PacienteResponse.model_validate(paciente) for paciente in pacientes]

    def obtener_paciente_por_id(self, paciente_id: int) -> PacienteResponse:
        paciente = self.repository.get_by_id(paciente_id)
        if not paciente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Paciente no encontrado"
            )
        return PacienteResponse.model_validate(paciente)

    def crear_paciente(self, paciente_data: PacienteCreate) -> PacienteResponse:
        if self.repository.get_by_cedula(paciente_data.cedula):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un paciente con esa cédula"
            )

        if self.repository.get_by_correo(paciente_data.correo):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un paciente con ese correo"
            )

        paciente = self.repository.create(paciente_data)
        return PacienteResponse.model_validate(paciente)

    def actualizar_paciente(self, paciente_id: int, paciente_data: PacienteUpdate) -> PacienteResponse:
        paciente = self.repository.get_by_id(paciente_id)
        if not paciente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Paciente no encontrado"
            )

        paciente_actualizado = self.repository.update(paciente, paciente_data)
        return PacienteResponse.model_validate(paciente_actualizado)

    def eliminar_paciente(self, paciente_id: int) -> dict:
        paciente = self.repository.get_by_id(paciente_id)
        if not paciente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Paciente no encontrado"
            )

        self.repository.delete(paciente)
        return {"message": "Paciente eliminado correctamente"}