from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from . import Base


class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    destination_id = Column(Integer, ForeignKey("destinations.id"))
    start_date = Column(Date)
    end_date = Column(Date)

    items = relationship("ItineraryItem", back_populates="itinerary")
    user = relationship("User", back_populates="itineraries")
    destination = relationship("Destination", back_populates="itineraries")

from .user import User
from .destination import Destination