from main import Uuid, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///UuidDatabase.db')

Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

userId = input("Enter the Id whose corresponding Uuid is to be deleted")
session.query(Uuid).all()
try:
    uuidToBeDeleted = session.query(Uuid).filter(Uuid.id == userId).one()
    session.delete(uuidToBeDeleted)
    session.commit()
    print("Uuid successfully deleted")
except:
    print("Unable to delete database")
