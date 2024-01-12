from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from . import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, index=True, unique=True)
    password = Column(String)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    dob = Column(Date)
    sex = Column(String)

    itineraries = relationship("Itinerary", back_populates="user", cascade="all, delete-orphan")
    travel_companion = relationship("TravelCompanion", uselist=False, back_populates="user")

    def create_itinerary(self, destination):
        from .itinerary import Itinerary  
        new_itinerary = Itinerary(user=self, destination=destination)
        return new_itinerary

from .itinerary import Itinerary