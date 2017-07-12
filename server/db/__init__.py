from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .event import TableEvent

engine = create_engine('sqlite:///marmot.db', echo=True)
DBSession = sessionmaker(bind=engine)
