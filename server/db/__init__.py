import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .event import TableEvent
from .user import TableUser
from .user_token import TableUserToken

engine = create_engine(f"sqlite:///{os.getcwd()}/marmot.db", echo=True)
DBSession = sessionmaker(bind=engine)
