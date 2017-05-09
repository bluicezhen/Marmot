from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import UUIDType

from database import engine

ModelBase = declarative_base()


class TableTag(ModelBase):
    __tablename__ = "tag"

    uuid = Column(UUIDType(binary=False), primary_key=True)
    name = Column(String(length=128), nullable=None, index=True)


if __name__ == "__main__":
    # Create Table "tag"
    ModelBase.metadata.create_all(engine)
