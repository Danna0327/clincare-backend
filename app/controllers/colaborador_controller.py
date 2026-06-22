from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.colaborador_schema import (
    ColaboradorCreate,
    ColaboradorResponse,
    ColaboradorUpdate
)
from app.services.colaborador_service import ColaboradorService

router = APIRouter(
    prefix="/colaboradores",
    tags=["Colaboradores"]
)


@router.get("/", response_model=List[ColaboradorResponse], summary="Listar colaboradores")
def listar_colaboradores(db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    return service.obtener_todos()


@router.get("/{colaborador_id}", response_model=ColaboradorResponse, summary="Obtener colaborador por ID")
def obtener_colaborador(colaborador_id: int, db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    colaborador = service.obtener_por_id(colaborador_id)
    if not colaborador:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Colaborador no encontrado"
        )
    return colaborador


@router.post("/", response_model=ColaboradorResponse, status_code=status.HTTP_201_CREATED, summary="Registrar colaborador")
def crear_colaborador(data: ColaboradorCreate, db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    return service.crear(data)


@router.put("/{colaborador_id}", response_model=ColaboradorResponse, summary="Actualizar colaborador")
def actualizar_colaborador(colaborador_id: int, data: ColaboradorUpdate, db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    colaborador = service.actualizar(colaborador_id, data)
    if not colaborador:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Colaborador no encontrado"
        )
    return colaborador


@router.delete("/{colaborador_id}", status_code=status.HTTP_200_OK, summary="Eliminar colaborador")
def eliminar_colaborador(colaborador_id: int, db: Session = Depends(get_db)):
    service = ColaboradorService(db)
    eliminado = service.eliminar(colaborador_id)
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Colaborador no encontrado"
        )
    return {"message": "Colaborador eliminado correctamente"}