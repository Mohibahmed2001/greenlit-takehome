from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL URL provided by ElephantSQL
SQLALCHEMY_DATABASE_URL = "postgresql://amdqpeop:KXDhDJTDJWBJaoXMeHAzQt5oINYJ_-SU@drona.db.elephantsql.com/amdqpeop"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
