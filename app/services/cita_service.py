from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.colaborador import Colaborador
from app.models.paciente import Paciente
from app.repositories.cita_repository import CitaRepository
from app.schemas.cita_schema import CitaCreate, CitaEstadoUpdate, CitaUpdate


class CitaService:
    """
    Lógica de negocio del módulo Cita.

    SOLID aplicado:
    - S (Single Responsibility):
      Esta clase solo contiene reglas de negocio de Cita.
    - D (Dependency Inversion):
      El controlador depende del servicio, y el servicio usa el repositorio.
    """

    def __init__(self, db: Session):
        self.db = db
        self.repository = CitaRepository(db)

    def listar_citas(self):
        return self.repository.get_all()

    def obtener_cita_por_id(self, cita_id: int):
        cita = self.repository.get_by_id(cita_id)
        if not cita:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cita no encontrada"
            )
        return cita

    def crear_cita(self, cita_data: CitaCreate):
        paciente = self.db.query(Paciente).filter(Paciente.id == cita_data.paciente_id).first()
        if not paciente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Paciente no encontrado"
            )

        medico = self.db.query(Colaborador).filter(Colaborador.id == cita_data.medico_id).first()
        if not medico:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Médico no encontrado"
            )

        if medico.rol != "MEDICO":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El colaborador seleccionado no es un médico"
            )

        return self.repository.create(cita_data)

    def actualizar_cita(self, cita_id: int, cita_data: CitaUpdate):
        cita = self.repository.get_by_id(cita_id)
        if not cita:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cita no encontrada"
            )

        paciente_id_final = cita_data.paciente_id if cita_data.paciente_id is not None else cita.paciente_id
        medico_id_final = cita_data.medico_id if cita_data.medico_id is not None else cita.medico_id

        paciente = self.db.query(Paciente).filter(Paciente.id == paciente_id_final).first()
        if not paciente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Paciente no encontrado"
            )

        medico = self.db.query(Colaborador).filter(Colaborador.id == medico_id_final).first()
        if not medico:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Médico no encontrado"
            )

        if medico.rol != "MEDICO":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El colaborador seleccionado no es un médico"
            )

        return self.repository.update(cita, cita_data)

    def eliminar_cita(self, cita_id: int):
        cita = self.repository.get_by_id(cita_id)
        if not cita:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cita no encontrada"
            )

        self.repository.delete(cita)
        return {"message": "Cita eliminada correctamente"}

    def cambiar_estado_cita(self, cita_id: int, estado_data: CitaEstadoUpdate):
        """
        Cambia el estado de una cita respetando reglas de negocio.

        Reglas:
        - Solo se puede cambiar a ATENDIDA o CANCELADA
        - Si la cita ya está ATENDIDA o CANCELADA, no puede cambiarse otra vez
        """
        cita = self.repository.get_by_id(cita_id)
        if not cita:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cita no encontrada"
            )

        if cita.estado in ["ATENDIDA", "CANCELADA"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"La cita ya se encuentra en estado {cita.estado} y no puede modificarse"
            )

        cita.estado = estado_data.estado
        self.db.commit()
        self.db.refresh(cita)

        return cita