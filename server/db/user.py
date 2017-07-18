from datetime import datetime
from hashlib import sha256
from typing import Dict, Union
from uuid import uuid5, NAMESPACE_URL
from sqlalchemy import Column, CHAR, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


class TableUser(declarative_base()):
    __tablename__ = "user"

    uuid = Column(CHAR(36), primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(CHAR(64), nullable=False)
    nickname = Column(String(256), nullable=False)
    time_create = Column(DateTime, nullable=False)

    def __init__(self, username: str, password: str, nickname: str):
        self.uuid = str(uuid5(NAMESPACE_URL, f"user:{username}"))
        self.username = username
        self.nickname = nickname
        self.time_create = datetime.now()
        self.password = sha256(f"{password}:{self.time_create.timestamp()}".encode("utf-8")).hexdigest()

    def to_dict(self) -> Dict[str, Union[str, int]]:
        return {
            "uuid": self.uuid,
            "username": self.username,
            "nickname": self.nickname,
            "time_create": int(self.time_create.timestamp())
        }
