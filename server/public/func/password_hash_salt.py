from datetime import datetime
from hashlib import sha256


def password_hash_salt(password: str, time: datetime) -> str:
    return sha256(f"{password}:{time.timestamp()}".encode("utf-8")).hexdigest()
