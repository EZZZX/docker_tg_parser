from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import postgresql
from time import time

tries = 0
engine = create_engine(postgresql)
Session = sessionmaker(bind=engine)

Base = declarative_base()
# try:
#     engine = create_engine(postgresql)
#     Session = sessionmaker(bind=engine)

#     Base = declarative_base()
# except Exception as error:
#     if tries < 3:
#         time.sleep(3) # give the DB a bit to recover if you want
#         tries+=1
#         engine = create_engine(postgresql)
#         Session = sessionmaker(bind=engine)

#         Base = declarative_base()
#     else:
#         raise error
# Base.metadata.create_all(engine)

# session = Session()


