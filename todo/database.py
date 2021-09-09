from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALHEMY_DATABASE_URL = 'postgresql://postgres:1998Betul@localhost/todo'

engine=create_engine(SQLALHEMY_DATABASE_URL,echo=True)


SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False,)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()