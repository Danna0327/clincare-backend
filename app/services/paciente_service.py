from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.paciente_repository import PacienteRepository
from app.schemas.paciente_schema import PacienteCreate, PacienteUpdate


class PacienteService:
    """
    Servicio que contiene la lógica de negocio del módulo Paciente.
    Principios SOLID:
    - S: centraliza la lógica de negocio del paciente.
    - D: depende del repositorio, no de detalles del controlador.
    """

    def __init__(self, db: Session):
        self.repository = PacienteRepository(db)

    def listar_pacientes(self) -> list:
        return self.repository.get_all()

    def obtener_paciente_por_id(self, paciente_id: int):
        paciente = self.repository.get_by_id(paciente_id)
        if not paciente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Paciente no encontrado"
            )
        return paciente

    def crear_paciente(self, paciente_data: PacienteCreate):
        paciente_existente = self.repository.get_by_cedula(paciente_data.cedula)
        if paciente_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un paciente con esa cédula"
            )

        correo_existente = self.repository.get_by_correo(paciente_data.correo)
        if correo_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un paciente con ese correo"
            )

        return self.repository.create(paciente_data)

    def actualizar_paciente(self, paciente_id: int, paciente_data: PacienteUpdate):
        paciente = self.repository.get_by_id(paciente_id)
        if not paciente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Paciente no encontrado"
            )

        if paciente_data.correo and paciente_data.correo != paciente.correo:
            correo_existente = self.repository.get_by_correo(paciente_data.correo)
            if correo_existente:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Ya existe un paciente con ese correo"
                )

        return self.repository.update(paciente, paciente_data)

    def eliminar_paciente(self, paciente_id: int):
        paciente = self.repository.get_by_id(paciente_id)
        if not paciente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Paciente no encontrado"
            )

        self.repository.delete(paciente)
        return {"message": "Paciente eliminado correctamente"}