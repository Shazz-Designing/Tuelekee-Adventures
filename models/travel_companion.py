from sqlalchemy import Column, Integer, String
from . import Base

class TravelCompanion(Base):
    __tablename__ = "travel_companions"

    id = Column(Integer, primary_key=True, index=True)