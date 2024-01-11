from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./tuelekeeadventures.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
