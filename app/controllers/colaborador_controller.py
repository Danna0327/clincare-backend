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