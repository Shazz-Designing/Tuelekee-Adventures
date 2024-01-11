from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)

    # Relationship with Itinerary
    itineraries = relationship("Itinerary", back_populates="user")

    # Relationship with TravelCompanion
    travel_companion = relationship("TravelCompanion", uselist=False, back_populates="user")
