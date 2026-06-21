from datetime import datetime
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    rol: Mapped[str] = mapped_column(String(30), nullable=False)  # ADMIN, MEDICO, RECEPCION
    estado: Mapped[str] = mapped_column(String(20), default="ACTIVO")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)