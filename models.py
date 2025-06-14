from sqlalchemy import Column, Integer, String, MetaData, Table
from database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)

metadata = Base.metadata
