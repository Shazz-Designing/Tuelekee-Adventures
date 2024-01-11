from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class ItineraryItem(Base):
    __tablename__ = "itinerary_items"

    id = Column(Integer, primary_key=True, index=True)

    # Relationship with Itinerary
    itinerary_id = Column(Integer, ForeignKey('itineraries.id'))
    itinerary = relationship("Itinerary", back_populates="items")

    # Relationship with Activity
    activity_id = Column(Integer, ForeignKey('activities.id'))
    activity = relationship("Activity", back_populates="itinerary_items")

    day = Column(Integer)
