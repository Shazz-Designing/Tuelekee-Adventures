from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tuelekee.models import Base
from tuelekee.config import SQLALCHEMY_DATABASE_URI

# Configure SQLite database
from tuelekee.config import SQLALCHEMY_DATABASE_URI, engine

# Create tables
Base.metadata.create_all(bind=engine)

