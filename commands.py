import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import UserBase
from models.destination import DestinationBase
from models.travel_companion import TravelCompanionBase
from models.itinerary import ItineraryBase
from models.activity import ActivityBase
from models.itinerary_item import ItineraryItemBase
from config import DATABASE_URL
from models import Base

# Configure SQLite database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Typer app instance
app = typer.Typer()

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to list users
@app.command(name='list-users')
def list_users():
    with get_db() as db:
        users = db.query(UserBase).all()
        typer.echo("List of Users:")
        for user in users:
            typer.echo(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Age: {user.age}")

# Function to list destinations
@app.command(name='list-destinations')
def list_destinations():
    with get_db() as db:
        destinations = db.query(DestinationBase).all()
        typer.echo("List of Destinations:")
        for destination in destinations:
            typer.echo(f"ID: {destination.id}, Name: {destination.name}")

# Function to list travel companions
@app.command(name='list-travel-companions')
def list_travel_companions():
    with get_db() as db:
        travel_companions = db.query(TravelCompanionBase).all()
        typer.echo("List of Travel Companions:")
        for companion in travel_companions:
            typer.echo(f"ID: {companion.id}, Name: {companion.name}, Age: {companion.age}")

# Function to list itineraries
@app.command(name='list-itineraries')
def list_itineraries():
    with get_db() as db:
        itineraries = db.query(ItineraryBase).all()
        typer.echo("List of Itineraries:")
        for itinerary in itineraries:
            typer.echo(f"ID: {itinerary.id}, Name: {itinerary.name}, User ID: {itinerary.user_id}")

# Function to list activities
@app.command(name='list-activities')
def list_activities():
    with get_db() as db:
        activities = db.query(ActivityBase).all()
        typer.echo("List of Activities:")
        for activity in activities:
            typer.echo(f"ID: {activity.id}, Name: {activity.name}")

if __name__ == '__main__':
    app()
