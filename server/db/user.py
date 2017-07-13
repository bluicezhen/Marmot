from datetime import datetime
from hashlib import sha256
from typing import Dict, Union
from uuid import uuid5, NAMESPACE_URL
from sqlalchemy import Column, CHAR, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


class TableUser(declarative_base()):
    __tablename__ = "user"

    uuid = Column(CHAR(36), primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(CHAR(64))
    nickname = Column(String(256))
    time_create = Column(DateTime)

    def __init__(self, username: str, password: str, nickname: str):
        self.uuid = str(uuid5(NAMESPACE_URL, f"user:{username}"))
        self.username = username
        self.nickname = nickname
        self.time_create = datetime.now()
        self.password = sha256(f"{password}:{self.time_create.timestamp()}").hexdigest()

    def to_dict(self) -> Dict[str, Union[str, int]]:
        return {
            "uuid": self.uuid,
            "username": self.username,
            "nickname": self.nickname,
            "time_create": int(self.time_create.timestamp())
        }
