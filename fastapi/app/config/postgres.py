from sqlalchemy.orm import Session 
from fastapi import  Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from typing_extensions import Annotated
import sys
from pathlib import Path
path = Path.cwd().parent
sys.path.append(str(path))

from database.get_url import postgres_url

# URL_DATABASE = os.getenv('POSTGRES_URL')
URL_DATABASE = postgres_url
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind=engine)

Base = declarative_base()


Base.metadata.create_all(bind=engine)     


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]