from main import Uuid, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///UuidDatabase.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

userInput = input("Enter the id whose corresponding uuid is to be fetched")
session.query(Uuid).all()
uuid = session.query(Uuid).filter(Uuid.id == userInput).first()

print(uuid.uniqueId)
