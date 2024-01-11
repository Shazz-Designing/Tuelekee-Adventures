from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .user import User
from .destination import Destination
from .travel_companion import TravelCompanion
from .itinerary import Itinerary
from .activity import Activity
from .itinerary_item import ItineraryItem
