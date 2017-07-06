from typing import Dict
from uuid import uuid5, NAMESPACE_URL
from sqlalchemy import Column, CHAR, String
from sqlalchemy.ext.declarative import declarative_base


class TableImage(declarative_base()):
    __tablename__ = "image"

    uuid = Column(CHAR(36), primary_key=True)
    title = Column(String(512))
    url = Column(String(512))

    def __init__(self, title: str, url: str):
        self.uuid = str(uuid5(NAMESPACE_URL, url))
        self.title = title
        self.url = url

    def to_dict(self) -> Dict[str, str]:
        return {
            "uuid": self.uuid,
            "title": self.title,
            "url": self.url
        }
