from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('db_user')
PWD = os.getenv('db_password')

Base = declarative_base()

engine = create_engine("postgresql://" + USER +
                       ":" + PWD + "@localhost:5432")

Session = sessionmaker(bind=engine)
