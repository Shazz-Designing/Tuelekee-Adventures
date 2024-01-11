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

def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()

def display_destinations(destinations):
    for idx, destination in enumerate(destinations, start=1):
        print(f"{idx}. {destination.name}")

def select_destination(destinations):
    display_destinations(destinations)
    while True:
        try:
            destination_choice = int(input("Select a destination (enter the corresponding number): "))
            selected_destination = destinations[destination_choice - 1]
            return selected_destination
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

def create_user():
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
    return user

def create_itinerary(user, selected_destination):
    itinerary_data = {
        "user_id": user.id,
        "destination_id": selected_destination.id,
        "start_date": "2024-01-15",
        "end_date": "2024-01-20"
    }
    itinerary = Itinerary(**itinerary_data)
    session.add(itinerary)
    session.commit()
    return itinerary

def select_activity(activities):
    while True:
        try:
            activity_choice = int(input("Select an activity (enter the corresponding number): "))
            selected_activity = activities[activity_choice - 1]
            return selected_activity
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

def add_activity_to_itinerary(itinerary, selected_activity):
    itinerary_item_data = {
        "itinerary_id": itinerary.id,
        "activity_id": selected_activity.id,
        "day": 1
    }
    itinerary_item = ItineraryItem(**itinerary_item_data)
    session.add(itinerary_item)
    session.commit()

def ask_for_travel_companion():
    return input("Do you want a travel companion? (yes/no): ").lower() == "yes"

def get_user_preferences():
    min_age = int(input("Enter minimum age preference: "))
    max_age = int(input("Enter maximum age preference: "))
    companion_sex = input("Enter preferred sex (Male/Female): ")
    return min_age, max_age, companion_sex

def display_available_companions(companions):
    print("Available travel companions:")
    for idx, companion in enumerate(companions, start=1):
        print(f"{idx}. {companion.name}, {companion.age} years old, {companion.sex}")

def select_travel_companion(companions):
    while True:
        try:
            companion_choice = int(input("Select a travel companion (enter the corresponding number): "))
            selected_companion = companions[companion_choice - 1]
            return selected_companion
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

def update_itinerary_with_companion(itinerary, selected_companion):
    itinerary.travel_companion_id = selected_companion.id
    session.commit()
    print(f"Travel companion {selected_companion.name} added to your itinerary!")

def display_user_details(user):
    print("User details:")
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Age: {user.age}")

def display_entire_itinerary(itinerary):
    print("\nEntire Itinerary:")
    print(f"Destination: {itinerary.destination.name}")
    for item in itinerary.items:
        print(f"Activity: {item.activity.name}")
        print(f"Date: {item.date}")

def display_travel_companion_details(user):
    if user.travel_companion:
        print("\nTravel Companion:")
        print(f"Name: {user.travel_companion.name}")
        print(f"Age: {user.travel_companion.age}")
        print(f"Sex: {user.travel_companion.sex}")

def create_user_journey():
    # User signs up
    user = create_user()

    # Select destination
    destinations = session.query(Destination).all()
    selected_destination = select_destination(destinations)

    # Create an itinerary
    itinerary = create_itinerary(user, selected_destination)

    # Select activities linked to the destination
    activities = session.query(Activity).filter_by(destination_id=selected_destination.id).all()
    selected_activity = select_activity(activities)

    # Add selected activity to the itinerary
    add_activity_to_itinerary(itinerary, selected_activity)

    # Ask user if they want a travel companion
    if ask_for_travel_companion():
        # Ask user for age range and sex preference
        min_age, max_age, companion_sex = get_user_preferences()

        # Find available travel companions based on user preferences
        available_companions = session.query(TravelCompanion).filter(
            TravelCompanion.age >= min_age,
            TravelCompanion.age <= max_age,
            TravelCompanion.sex == companion_sex
        ).all()

        if available_companions:
            # Display available companions
            display_available_companions(available_companions)

            # Select a travel companion
            selected_companion = select_travel_companion(available_companions)

            # Update user's itinerary with the selected travel companion
            update_itinerary_with_companion(itinerary, selected_companion)

        else:
            print("No available travel companions matching your preferences.")

    print("User journey created successfully!")

if __name__ == "__main__":
    create_user_journey()

    # Fetching user details from the database
    user = get_user_by_email('john.doe@example.com')

    # Fetching entire itinerary based on user choices
    itinerary = session.query(Itinerary).filter_by(user_id=user.id).first()

    # Example print statements to display user details and entire itinerary
    display_user_details(user)
    display_entire_itinerary(itinerary)

    # Additional logic for displaying travel companion details if applicable
    display_travel_companion_details(user)
