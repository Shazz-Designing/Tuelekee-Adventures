from sqlalchemy import Column, Integer, String
from . import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
