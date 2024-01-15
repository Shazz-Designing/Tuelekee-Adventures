import click
from cli import Session
from models import Destination, Activity

@click.group()
def destinations_cli():
    pass

@destinations_cli.command()
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
    destinations_cli()
