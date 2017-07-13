from datetime import datetime
from hashlib import sha256
from uuid import uuid5, NAMESPACE_URL
from sqlalchemy import Column, CHAR, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from .user import TableUser


class TableUserToken(declarative_base()):
    __tablename__ = "user_token"

    uuid = Column(CHAR(36), primary_key=True)
    user_uuid = Column(CHAR(36), ForeignKey(TableUser.uuid, onupdate="CASCADE", ondelete="CASCADE"))
    token = Column(CHAR(64))
    time_create = Column(DateTime)

    def __init__(self, user_uuid: str):
        self.time_create = datetime.now()
        self.uuid = str(uuid5(NAMESPACE_URL, f"token:{user_uuid}:{self.time_create.timestamp()}"))
        self.user_uuid = user_uuid
        self.token = sha256(self.uuid.encode("utf-8")).hexdigest()
