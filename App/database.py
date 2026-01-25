from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String
from dotenv import load_dotenv
import os

### this is load the environment variable 
load_dotenv()

Database_link = os.getenv("DATABASE_URL")
if Database_link:
       Engine = create_engine(Database_link)
       Session_local  = sessionmaker(autoflush=False,bind=Engine)

Base = declarative_base()

# creating the schema for the table to bind to the base for creation of table in the postgresql 
class Blog(Base):
    __tablename__ = 'blogs'
    ids = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    title = Column(String)
    description = Column(String)

    class config():
        orm_model = True

class find(Base):
    __tablename__ = 'id'
    id = Column(Integer,primary_key=True,index=True)


def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()


def create_table():
    Base.metadata.create_all(bind=Engine)












