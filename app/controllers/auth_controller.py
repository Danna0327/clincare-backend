#COMMIT 14 — auth controller

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.usuario_repository import UsuarioRepository
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    try:
        repo = UsuarioRepository(db)
        service = AuthService(repo)
        return service.login(username, password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))