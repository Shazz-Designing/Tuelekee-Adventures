from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.itinerary import Itinerary

Base = declarative_base()

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Relationships
    activities = relationship("Activity", back_populates="destination")
    itineraries = relationship("Itinerary", back_populates="destination")
