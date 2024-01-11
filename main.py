from sqlalchemy.orm import sessionmaker
from models.user import User
from models.destination import Destination
from models.travel_companion import TravelCompanion
from models.itinerary import Itinerary
from models.activity import Activity
from models.itinerary_item import ItineraryItem
from database import Base, engine

Base.metadata.bind = engine
Base.metadata.create_all()

Session = sessionmaker(bind=engine)
session = Session()

def create_user_journey():
    # User signs up
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "dob": "1990-01-15",
        "sex": "Male"
    }
    user = User(**user_data)
    session.add(user)
    session.commit()

    # Select destination
    available_destinations = session.query(Destination).all()
    for idx, destination in enumerate(available_destinations, start=1):
        print(f"{idx}. {destination.name}")

    destination_choice = int(input("Select a destination (enter the corresponding number): "))
    selected_destination = available_destinations[destination_choice - 1]

    # Create an itinerary
    itinerary_data = {
        "user_id": user.id,
        "destination_id": selected_destination.id,
        "start_date": "2024-01-15",
        "end_date": "2024-01-20"
    }
    itinerary = Itinerary(**itinerary_data)
    session.add(itinerary)
    session.commit()

    # Select activities linked to the destination
    available_activities = session.query(Activity).filter_by(destination_id=selected_destination.id).all()
    for idx, activity in enumerate(available_activities, start=1):
        print(f"{idx}. {activity.name}")

    activity_choice = int(input("Select an activity (enter the corresponding number): "))
    selected_activity = available_activities[activity_choice - 1]

    # Add selected activity to the itinerary
    itinerary_item_data = {
        "itinerary_id": itinerary.id,
        "activity_id": selected_activity.id,
        "day": 1
    }
    itinerary_item = ItineraryItem(**itinerary_item_data)
    session.add(itinerary_item)
    session.commit()

    # Ask user if they want a travel companion
    companion_choice = input("Do you want a travel companion? (yes/no): ")

    if companion_choice.lower() == "yes":
        # Ask user for age range and sex preference
        min_age = int(input("Enter minimum age preference: "))
        max_age = int(input("Enter maximum age preference: "))
        companion_sex = input("Enter preferred sex (Male/Female): ")

        # Find available travel companions based on user preferences
        available_companions = session.query(TravelCompanion).filter(
            TravelCompanion.age >= min_age,
            TravelCompanion.age <= max_age,
            TravelCompanion.sex == companion_sex
        ).all()

        if available_companions:
            # Display available companions
            print("Available travel companions:")
            for idx, companion in enumerate(available_companions, start=1):
                print(f"{idx}. {companion.name}, {companion.age} years old, {companion.sex}")

            companion_choice = int(input("Select a travel companion (enter the corresponding number): "))
            selected_companion = available_companions[companion_choice - 1]

            # Update user's itinerary with the selected travel companion
            itinerary.travel_companion_id = selected_companion.id
            session.commit()

            print(f"Travel companion {selected_companion.name} added to your itinerary!")

        else:
            print("No available travel companions matching your preferences.")

    print("User journey created successfully!")

if __name__ == "__main__":
    create_user_journey()

    # Fetching user details from the database (replace with your actual logic)
    user = session.query(User).filter_by(email='john.doe@example.com').first()

    # Fetching entire itinerary based on user choices (replace with your actual logic)
    itinerary = session.query(Itinerary).filter_by(user_id=user.id).first()

    # Example print statements to display user details and entire itinerary
    print("User details:")
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Age: {user.age}")

    print("\nEntire Itinerary:")
    print(f"Destination: {itinerary.destination.name}")
    
    for item in itinerary.items:
        print(f"Activity: {item.activity.name}")
        print(f"Date: {item.date}")

    # Additional logic for displaying travel companion details if applicable
    if user.travel_companion:
        print("\nTravel Companion:")
        print(f"Name: {user.travel_companion.name}")
        print(f"Age: {user.travel_companion.age}")
        print(f"Sex: {user.travel_companion.sex}")
