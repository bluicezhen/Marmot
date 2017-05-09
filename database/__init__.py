from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import table

engine = create_engine(f"mysql+pymysql://root:123698745@localhost:3306/marmot?charset=utf8", pool_recycle=60)
DBSession = sessionmaker(bind=engine)
