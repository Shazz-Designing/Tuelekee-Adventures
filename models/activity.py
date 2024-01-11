from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # Relationship with Destination
    destination_id = Column(Integer, ForeignKey('destinations.id'))
    destination = relationship("Destination", back_populates="activities")

    # Relationship with ItineraryItem
    itinerary_items = relationship("ItineraryItem", back_populates="activity")
