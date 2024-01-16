from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# User, Itinerary, Destination, and Activity tables with relationships
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    itineraries = relationship('Itinerary', back_populates='user')
    
    def __init__(self, name, email, age=None):
        self.name = name
        self.email = email
        self.age = age

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
    destination_id = Column(Integer, ForeignKey('destinations.id'))
    destination = relationship('Destination', back_populates='activities')
    
    __table_args__ = {'extend_existing': True}

class Destination(Base):
    __tablename__ = 'destinations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    activities = relationship('Activity', back_populates='destination')

engine = create_engine("sqlite:///tuelekee.db")