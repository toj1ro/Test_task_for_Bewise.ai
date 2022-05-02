from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/base_of_questions"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session = Session(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
