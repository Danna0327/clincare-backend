#COMMIT 18 — colaborador controller

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.colaborador_repository import ColaboradorRepository
from app.services.colaborador_service import ColaboradorService

router = APIRouter(prefix="/colaboradores", tags=["Colaboradores"])

@router.post("/")
def crear(data: dict, db: Session = Depends(get_db)):
    repo = ColaboradorRepository(db)
    service = ColaboradorService(repo)
    return service.crear(data)

@router.get("/")
def listar(db: Session = Depends(get_db)):
    repo = ColaboradorRepository(db)
    service = ColaboradorService(repo)
    return service.listar()