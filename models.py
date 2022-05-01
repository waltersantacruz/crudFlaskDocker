from sqlalchemy import Column, String, Integer
from database import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    phone = Column(String(30))

Base.metadata.create_all(engine)
