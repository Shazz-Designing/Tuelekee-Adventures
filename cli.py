import click
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Activity, Destination, Itinerary

engine = create_engine("sqlite:///tuelekee.db")  # Adjust the database URL as needed
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
def list_users():
    """List all users in the database."""
    session = Session()
    users = session.query(User).all()
    for user in users:
        click.echo(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")
    session.close()

@cli.command()
@click.argument('user_id', type=int)
def view_user(user_id):
    """View details of a specific user."""
    session = Session()
    user = session.query(User).get(user_id)
    if user:
        click.echo(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")
    else:
        click.echo(f"User with ID {user_id} not found.")
    session.close()

# Commands for creating users
@cli.command()
@click.option('--first-name', prompt='Enter your first name', help='First name of the user')
@click.option('--last-name', prompt='Enter your last name', help='Last name of the user')
@click.option('--email', prompt='Enter your email address', help='Email address of the user')
@click.option('--dob', prompt='Enter your date of birth (YYYY-MM-DD)', help='Date of birth of the user')
def register(first_name, last_name, email, dob):
    """Register a new user."""
    try:
        dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
    except ValueError:
        click.echo("Invalid date format. Please use the format YYYY-MM-DD.")
        return
    
    # Calculate age
    today = datetime.now().date()
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

    session = Session()
    new_user = User(name=f"{first_name} {last_name}", email=email, age=age)
    session.add(new_user)
    session.commit()
    
    click.echo(f"New user regsitered with the following details:")
    click.echo(f"User ID: {new_user.id}")
    click.echo(f"Name: {new_user.name}")
    click.echo(f"Email: {new_user.email}")
    click.echo(f"Age: {new_user.age}")

    session.close()


# Commands for managing activities
@cli.command()
def list_activities():
    """List all activities in the database."""
    session = Session()
    activities = session.query(Activity).all()
    for activity in activities:
        click.echo(f"Activity ID: {activity.id}, Name: {activity.name}")
    session.close()

@cli.command()
@click.argument('activity_id', type=int)
def view_activity(activity_id):
    """View details of a specific activity."""
    session = Session()
    activity = session.query(Activity).get(activity_id)
    if activity:
        click.echo(f"Activity ID: {activity.id}, Name: {activity.name}")
    else:
        click.echo(f"Activity with ID {activity_id} not found.")
    session.close()

@cli.command()
@click.argument('name')
def add_activity(name):
    """Add a new activity to the database."""
    session = Session()
    new_activity = Activity(name=name)
    session.add(new_activity)
    session.commit()
    click.echo(f"Activity {name} added successfully with ID: {new_activity.id}")
    session.close()


@cli.command()
def list_destinations():
    """List all destinations and their activities."""
    session = Session()
    destinations = session.query(Destination).all()
    for destination in destinations:
        click.echo(f"Destination ID: {destination.id}, Name: {destination.name}")
        click.echo("Activities:")
        for activity in destination.activities:
            click.echo(f"  - Activity ID: {activity.id}, Name: {activity.name}")
    session.close()


@cli.command()
@click.argument('user_id', type=int)
def create_itinerary(user_id):
    """Create a new travel itinerary."""
    session = Session()

    # Check if the user exists
    user = session.query(User).get(user_id)
    if not user:
        click.echo(f"User with ID {user_id} not found.")
        session.close()
        return

    click.echo(f"Creating itinerary for {user.name}")

    # Display list of destinations
    destinations = session.query(Destination).all()
    click.echo("Available Destinations:")
    for destination in destinations:
        click.echo(f"Destination ID: {destination.id}, Name: {destination.name}")

    destination_id = click.prompt("Enter the ID of the selected destination", type=int)

    # Display activities for the selected destination
    destination = session.query(Destination).get(destination_id)
    if destination:
        click.echo(f"Activities for {destination.name}:")
        for activity in destination.activities:
            click.echo(f"Activity ID: {activity.id}, Name: {activity.name}")

        activity_id = click.prompt("Enter the ID of the selected activity", type=int)

        # Ask if user wants a travel companion
        travel_companion = click.confirm("Do you want a travel companion?")

        # Create itinerary
        new_itinerary = Itinerary(user=user, destination=destination, activity_id=activity_id, travel_companion=travel_companion)
        session.add(new_itinerary)
        session.commit()

        click.echo("Itinerary created successfully!")
        click.echo("Itinerary Details:")
        click.echo(f"User: {user.name}")
        click.echo(f"Destination: {destination.name}")
        click.echo(f"Activity: {activity.name}")
        click.echo(f"Travel Companion: {'Yes' if travel_companion else 'No'}")

    else:
        click.echo(f"Destination with ID {destination_id} not found.")

    session.close()

if __name__ == '__main__':
    cli()