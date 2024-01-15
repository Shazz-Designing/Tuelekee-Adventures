import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Activity, Destination

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

@cli.command()
@click.argument('name')
@click.option('--age', default=25, help='Specify the age (default is 25)')
def add_user(name, age):
    """Add a new user to the database."""
    session = Session()
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    click.echo(f"User {name} added successfully with ID: {new_user.id}")
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


if __name__ == '__main__':
    cli()
