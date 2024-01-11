from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)

    # Relationship with User
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="itineraries")

    # Relationship with Destination
    destination_id = Column(Integer, ForeignKey('destinations.id'))
    destination = relationship("Destination", back_populates="itineraries")

    # Relationship with TravelCompanion
    travel_companion_id = Column(Integer, ForeignKey('travel_companions.id'))
    travel_companion = relationship("TravelCompanion", back_populates="itineraries")

    # Relationship with ItineraryItem
    items = relationship("ItineraryItem", back_populates="itinerary")
