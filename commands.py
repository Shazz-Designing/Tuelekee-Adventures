import typer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.user import Base as UserBase
from models.destination import Base as DestinationBase
from models.travel_companion import Base as TravelCompanionBase
from models.itinerary import Base as ItineraryBase
from models.activity import Base as ActivityBase
from models.itinerary_item import Base as ItineraryItemBase
from config import DATABASE_URL
from models import Base as AllModelsBase

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
def list_users(db: Session = typer.Depends(get_db)):
    users = db.query(UserBase).all()
    typer.echo("List of Users:")
    for user in users:
        typer.echo(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Age: {user.age}")

# Function to list destinations
@app.command(name='list-destinations')
def list_destinations(db: Session = typer.Depends(get_db)):
    destinations = db.query(DestinationBase).all()
    typer.echo("List of Destinations:")
    for destination in destinations:
        typer.echo(f"ID: {destination.id}, Name: {destination.name}")

# Function to list travel companions
@app.command(name='list-travel-companions')
def list_travel_companions(db: Session = typer.Depends(get_db)):
    travel_companions = db.query(TravelCompanionBase).all()
    typer.echo("List of Travel Companions:")
    for companion in travel_companions:
        typer.echo(f"ID: {companion.id}, Name: {companion.name}, Age: {companion.age}")

# Function to list itineraries
@app.command(name='list-itineraries')
def list_itineraries(db: Session = typer.Depends(get_db)):
    itineraries = db.query(ItineraryBase).all()
    typer.echo("List of Itineraries:")
    for itinerary in itineraries:
        typer.echo(f"ID: {itinerary.id}, Name: {itinerary.name}, User ID: {itinerary.user_id}")

# Function to list activities
@app.command(name='list-activities')
def list_activities(db: Session = typer.Depends(get_db)):
    activities = db.query(ActivityBase).all()
    typer.echo("List of Activities:")
    for activity in activities:
        typer.echo(f"ID: {activity.id}, Name: {activity.name}")

if __name__ == '__main__':
    app()
