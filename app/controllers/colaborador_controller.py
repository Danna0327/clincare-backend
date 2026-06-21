
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.colaborador_repository import ColaboradorRepository
from app.services.colaborador_service import ColaboradorService

router = APIRouter(prefix="/colaboradores")

def get_service(db: Session):
    return ColaboradorService(ColaboradorRepository(db))

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return get_service(db).listar()

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.colaborador_schema import (
    ColaboradorCreate,
    ColaboradorResponse,
    ColaboradorUpdate,
)
from app.services.colaborador_service import ColaboradorService

router = APIRouter(
    prefix="/api/colaboradores",
    tags=["Colaboradores"]
)


@router.get("/", response_model=list[ColaboradorResponse], status_code=status.HTTP_200_OK)
def listar_colaboradores(db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    return service.listar_colaboradores()


@router.get("/medicos", response_model=list[ColaboradorResponse], status_code=status.HTTP_200_OK)
def listar_medicos(db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    return service.listar_medicos()


@router.get("/administrativos", response_model=list[ColaboradorResponse], status_code=status.HTTP_200_OK)
def listar_administrativos(db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    return service.listar_administrativos()


@router.get("/{colaborador_id}", response_model=ColaboradorResponse, status_code=status.HTTP_200_OK)
def obtener_colaborador(colaborador_id: int, db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    return service.obtener_colaborador_por_id(colaborador_id)


@router.post("/", response_model=ColaboradorResponse, status_code=status.HTTP_201_CREATED)
def crear_colaborador(colaborador_data: ColaboradorCreate, db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    return service.crear_colaborador(colaborador_data)


@router.put("/{colaborador_id}", response_model=ColaboradorResponse, status_code=status.HTTP_200_OK)
def actualizar_colaborador(
    colaborador_id: int,
    colaborador_data: ColaboradorUpdate,
    db: Session = Depends(get_db)
):
    service = ColaboradorService(db)
    return service.actualizar_colaborador(colaborador_id, colaborador_data)


@router.delete("/{colaborador_id}", status_code=status.HTTP_200_OK)
def eliminar_colaborador(colaborador_id: int, db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    return service.eliminar_colaborador(colaborador_id)

