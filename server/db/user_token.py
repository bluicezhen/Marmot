from datetime import datetime
from hashlib import sha256
from uuid import uuid5, NAMESPACE_URL
from sqlalchemy import Column, CHAR, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from .user import TableUser


class TableUserToken(declarative_base()):
    __tablename__ = "user_token"

    uuid = Column(CHAR(36), primary_key=True)
    user_uuid = Column(CHAR(36), ForeignKey(TableUser.uuid, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    token = Column(CHAR(64), nullable=False)
    time_create = Column(DateTime, nullable=False, default=datetime.now)
    time_update = Column(DateTime, nullable=False)

    def __init__(self, user_uuid: str):
        self.time_create = datetime.now()
        self.time_update = self.time_create
        self.uuid = str(uuid5(NAMESPACE_URL, f"token:{user_uuid}:{self.time_create.timestamp()}"))
        self.user_uuid = user_uuid
        self.token = sha256(self.uuid.encode("utf-8")).hexdigest()

    def to_dict(self) -> dict:
        return {
            "user_uuid": self.user_uuid,
            "token": self.token
        }
