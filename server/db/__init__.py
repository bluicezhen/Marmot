from sqlalchemy import create_engine
from .event import TableEvent

engine = create_engine('sqlite:///marmot.db', echo=True)
