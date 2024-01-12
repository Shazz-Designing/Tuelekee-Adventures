from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class ItineraryItem(Base):
    __tablename__ = "itinerary_items"

    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))
    day = Column(Integer)

    itinerary = relationship("Itinerary", back_populates="items")
    activity = relationship("Activity", back_populates="itinerary_items")
