from datetime import datetime
from time import time
from typing import Dict
from uuid import uuid5, NAMESPACE_URL
from sqlalchemy import Column, CHAR, DateTime, ForeignKey, String, Text
from sqlalchemy.ext.declarative import declarative_base
from .user import TableUser


class TableEvent(declarative_base()):
    __tablename__ = "event"

    uuid = Column(CHAR(36), primary_key=True)
    user_uuid = Column(CHAR(36), ForeignKey(TableUser.uuid, onupdate="CASCADE", ondelete="CASCADE"))
    title = Column(String(512), nullable=False)
    desc = Column(Text, default="")
    time_begin = Column(DateTime, nullable=False)
    time_end = Column(DateTime, nullable=False)

    def __init__(self, user_uuid: str, title: str, desc: str, time_begin: datetime, time_end: datetime):
        self.uuid = str(uuid5(NAMESPACE_URL, f"{self.__tablename__}:{time()}:{title}"))
        self.user_uuid = user_uuid
        self.title = title
        self.desc = desc
        self.time_begin = time_begin
        self.time_end = time_end

    def to_dict(self) -> Dict[str, str]:
        return {
            "uuid": self.uuid,
            "user_uuid": self.user_uuid,
            "title": self.title,
            "desc": self.desc,
            "time_begin": int(self.time_begin.timestamp()),
            "time_end": int(self.time_end.timestamp())
        }
