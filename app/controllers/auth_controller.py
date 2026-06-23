from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.usuario_repository import UsuarioRepository
from app.services.auth_service import AuthService
from app.schemas.auth_schema import LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_service(db: Session):
    repo = UsuarioRepository(db)
    return AuthService(repo)

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    service = get_service(db)
    try:
        return service.login(data)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))