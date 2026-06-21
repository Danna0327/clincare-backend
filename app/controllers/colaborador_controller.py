from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.colaborador_repository import ColaboradorRepository
from app.services.colaborador_service import ColaboradorService
from app.schemas.colaborador_schema import ColaboradorCreate

router = APIRouter(prefix="/colaboradores")

def get_service(db: Session):
    return ColaboradorService(ColaboradorRepository(db))

@router.post("/")
def crear(data: ColaboradorCreate, db: Session = Depends(get_db)):
    service = get_service(db)
    return service.crear(data)