import random
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base, Uuid

uuid = ""
def createUuid():
     global uuid
     year = str(datetime.datetime.now().year)
     month = str(datetime.datetime.now().month)
     day = str(datetime.datetime.now().day)
     hour = str(datetime.datetime.now().hour)
     minute = str(datetime.datetime.now().minute)
     second = str(datetime.datetime.now().second)
     microsecond = str(datetime.datetime.now().microsecond)
     uuid = year + month + day + hour + minute + second + microsecond
     return uuid

createUuid()

engine = create_engine('sqlite:///UuidDatabase.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
uuidData = Uuid(uniqueId=uuid)
session.add(uuidData)
try:
     session.commit()
     print("Uuid successfully saved to the database")
     session.close()
     # exit()
except IOError:
    print("Error in inserting uuid to database")
