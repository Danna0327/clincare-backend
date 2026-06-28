import hashlib
from datetime import datetime, timedelta, timezone
from typing import Any, Dict


def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str):
    return hash_password(password) == hashed


def create_access_token(payload: Dict[str, Any]) -> str:
    return f"token::{payload.get('sub', 'unknown')}::{payload.get('rol', 'user')}"