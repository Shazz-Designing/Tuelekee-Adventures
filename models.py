from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Boolean
from sqlalchemy.orm import declarative_base, relationship, Session, joinedload

Base = declarative_base()

# Define the association table for many-to-many relationship
itinerary_activity_association = Table(
    'itinerary_activity_association',
    Base.metadata,
    Column('itinerary_id', Integer, ForeignKey('itineraries.id')),
    Column('activity_id', Integer, ForeignKey('activities.id'))
)

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

class Destination(Base):
    __tablename__ = 'destinations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    activities = relationship('Activity', back_populates='destination')
    itineraries = relationship('Itinerary', back_populates='destination')

class Itinerary(Base):
    __tablename__ = 'itineraries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    destination_id = Column(Integer, ForeignKey('destinations.id', deferrable=True, initially="DEFERRED"), nullable=True)
    travel_companion = Column(Boolean, nullable=False)

    # Relationship with User
    user = relationship('User', back_populates='itineraries')

    # Relationship with Destination
    destination = relationship('Destination', back_populates='itineraries')

    # Relationship with Activity
    activities = relationship('Activity', secondary=itinerary_activity_association, back_populates='itineraries')


    def __repr__(self):
        user_name = self.user.name if self.user else "Unknown User"
        destination_name = self.destination.name if self.destination else "Unknown Destination"

        return (
            f"Itinerary ID: {self.id}\n"
            f"User: {user_name}\n"
            f"Destination: {destination_name}\n"
            f"Travel Companion: {'Yes' if self.travel_companion else 'No'}"
        )


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    destination_id = Column(Integer, ForeignKey('destinations.id'))
    destination = relationship('Destination', back_populates='activities')
    itineraries = relationship('Itinerary', secondary=itinerary_activity_association, back_populates='activities')
    
    __table_args__ = {'extend_existing': True}

# Create the SQLite database engine
engine = create_engine("sqlite:///tuelekee.db")

# Recreate the tables
Base.metadata.create_all(engine)

# Create a session
session = Session(engine)

