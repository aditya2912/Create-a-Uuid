from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Uuid(Base):
     __tablename__ = 'uuid'
     id = Column(Integer, primary_key=True, autoincrement=True)
     uniqueId = Column(String)

engine = create_engine('sqlite:///UuidDatabase.db')
Base.metadata.create_all(engine)
