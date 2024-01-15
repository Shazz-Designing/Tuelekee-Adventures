from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# User, Itinerary, Destination and Activity tables with relationships
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    itineraries = relationship('Itinerary', back_populates='user')

class Itinerary(Base):
    __tablename__ = 'itineraries'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='itineraries')
    activities = relationship('Activity', secondary='itinerary_activity_association')

itinerary_activity_association = Table(
    'itinerary_activity_association',
    Base.metadata,
    Column('itinerary_id', Integer, ForeignKey('itineraries.id')),
    Column('activity_id', Integer, ForeignKey('activities.id'))
)

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Destination(Base):
    __tablename__ = 'destinations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    activities = relationship('Activity', secondary='activity_destination_association')

activity_destination_association = Table(
    'activity_destination_association',
    Base.metadata,
    Column('activity_id', Integer, ForeignKey('activities.id')),
    Column('destination_id', Integer, ForeignKey('destinations.id'))
)
