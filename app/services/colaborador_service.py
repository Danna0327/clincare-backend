
from app.repositories.colaborador_repository import ColaboradorRepository

class ColaboradorService:

    def __init__(self, repo: ColaboradorRepository):
        self.repo = repo

    def listar(self):
        return self.repo.get_all()

    def crear(self, data):
        if data.tipo_colaborador not in ["MEDICO", "ADMINISTRATIVO"]:
            raise ValueError("Tipo inválido")

        return self.repo.create(data)

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.colaborador_repository import ColaboradorRepository
from app.schemas.colaborador_schema import ColaboradorCreate, ColaboradorUpdate


class ColaboradorService:
    """
    Lógica de negocio del módulo Colaborador.
    SOLID:
    - S: concentra reglas del colaborador
    - D: depende del repositorio, no del controlador
    """

    def __init__(self, db: Session):
        self.repository = ColaboradorRepository(db)

    def listar_colaboradores(self):
        return self.repository.get_all()

    def listar_medicos(self):
        return self.repository.get_medicos()

    def listar_administrativos(self):
        return self.repository.get_administrativos()

    def obtener_colaborador_por_id(self, colaborador_id: int):
        colaborador = self.repository.get_by_id(colaborador_id)
        if not colaborador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Colaborador no encontrado"
            )
        return colaborador

    def crear_colaborador(self, colaborador_data: ColaboradorCreate):
        existente_cedula = self.repository.get_by_cedula(colaborador_data.cedula)
        if existente_cedula:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un colaborador con esa cédula"
            )

        existente_correo = self.repository.get_by_correo(colaborador_data.correo)
        if existente_correo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un colaborador con ese correo"
            )

        if colaborador_data.rol == "MEDICO" and not colaborador_data.especialidad:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Un médico debe tener especialidad registrada"
            )

        if colaborador_data.rol == "ADMINISTRATIVO":
            colaborador_data.especialidad = None

        return self.repository.create(colaborador_data)

    def actualizar_colaborador(self, colaborador_id: int, colaborador_data: ColaboradorUpdate):
        colaborador = self.repository.get_by_id(colaborador_id)
        if not colaborador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Colaborador no encontrado"
            )

        if colaborador_data.correo and colaborador_data.correo != colaborador.correo:
            existente_correo = self.repository.get_by_correo(colaborador_data.correo)
            if existente_correo:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Ya existe un colaborador con ese correo"
                )

        rol_final = colaborador_data.rol if colaborador_data.rol is not None else colaborador.rol
        especialidad_final = (
            colaborador_data.especialidad
            if colaborador_data.especialidad is not None
            else colaborador.especialidad
        )

        if rol_final == "MEDICO" and not especialidad_final:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Un médico debe tener especialidad registrada"
            )

        if rol_final == "ADMINISTRATIVO":
            colaborador_data.especialidad = None

        return self.repository.update(colaborador, colaborador_data)

    def eliminar_colaborador(self, colaborador_id: int):
        colaborador = self.repository.get_by_id(colaborador_id)
        if not colaborador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Colaborador no encontrado"
            )

        self.repository.delete(colaborador)
        return {"message": "Colaborador eliminado correctamente"}

