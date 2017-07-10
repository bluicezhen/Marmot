from datetime import datetime
from time import time
from typing import Dict
from uuid import uuid5, NAMESPACE_URL
from sqlalchemy import Column, CHAR, DateTime, String, Text
from sqlalchemy.ext.declarative import declarative_base


class TableEvent(declarative_base()):
    __tablename__ = "event"

    uuid = Column(CHAR(36), primary_key=True)
    title = Column(String(512))
    desc = Column(Text)
    time_begin = Column(DateTime)
    time_end = Column(DateTime)

    def __init__(self, title: str, desc: str, time_begin: datetime, time_end: datetime):
        self.uuid = str(uuid5(NAMESPACE_URL, f"{self.__tablename__}:{time()}:{title}"))
        self.title = title
        self.desc = desc
        self.time_begin = time_begin
        self.time_end = time_end

    def to_dict(self) -> Dict[str, str]:
        return {
            "uuid": self.uuid,
            "title": self.title,
            "desc": self.desc,
            "time_begin": int(self.time_begin.timestamp()),
            "time_end": int(self.time_end.timestamp())
        }
