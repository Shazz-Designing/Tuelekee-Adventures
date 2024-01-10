from sqlalchemy import Column, Integer, String
from . import Base

class ItineraryItem(Base):
    __tablename__ = "itinerary_items"

    id = Column(Integer, primary_key=True, index=True)