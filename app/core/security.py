import hashlib
import base64
import json
from datetime import datetime, timedelta

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed

def create_token(data: dict, minutes: int = 60):
    payload = data.copy()
    payload["exp"] = (datetime.utcnow() + timedelta(minutes=minutes)).isoformat()
    return base64.b64encode(json.dumps(payload).encode()).decode()