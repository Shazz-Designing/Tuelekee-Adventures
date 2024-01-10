# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Destination, TravelCompanion, Itinerary, Activity, ItineraryItem, Base

# Configure SQLite database
DATABASE_URL = 'sqlite:///tuelekee_adventures.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables (if not existing)
Base.metadata.create_all(bind=engine)

# Seed Data
def seed_data():
    # Create a database session
    db = SessionLocal()

    try:
        # Seed Users
        users_data = [
            {'username': 'Sharon A', 'email': 'sharon.a@gmail.com', 'age': 28},
            {'username': 'Allison W', 'email': 'allison.w@hotmail.com', 'age': 35},
            {'username': 'Hazel K', 'email': 'hazel.k@yahoo.com', 'age': 42},
            {'username': 'Geraldine M', 'email': 'geraldine.m@aol.com', 'age': 50},
            {'username': 'Simon O', 'email': 'simon.o@outlook.com', 'age': 23},
            {'username': 'Erick K', 'email': 'erick.k@protonmail.com', 'age': 31},
            {'username': 'Dickson K', 'email': 'dickson.k@icloud.com', 'age': 45},
            {'username': 'Earl M', 'email': 'earl.m@live.com', 'age': 36},
            {'username': 'Sidra O', 'email': 'sidra.o@yandex.com', 'age': 27},
            {'username': 'James O', 'email': 'james.o@rediffmail.com', 'age': 29},
        ]

        for user_data in users_data:
            user = User(**user_data)
            db.add(user)

        # Seed Destinations
        destinations_data = [
            {'name': 'Serengeti National Park, Tanzania'},
            {'name': 'Victoria Falls, Zambia'},
            {'name': 'Marrakech, Morocco'},
            {'name': 'Table Mountain, South Africa'},
            {'name': 'Pyramids of Giza, Egypt'},
            {'name': 'Mount Kilimanjaro, Tanzania'},
            {'name': 'Okavango Delta, Botswana'},
            {'name': 'Timbuktu, Mali'},
            {'name': 'Namib Desert, Namibia'},
            {'name': 'Maasai Mara, Kenya'},
        ]

        for destination_data in destinations_data:
            destination = Destination(**destination_data)
            db.add(destination)

        # Seed Travel Companions
        travel_companions_data = [
            {'name': 'Sharon A', 'age': 28},
            {'name': 'Allison W', 'age': 35},
            {'name': 'Hazel K', 'age': 42},
            {'name': 'Geraldine M', 'age': 50},
            {'name': 'Simon O', 'age': 23},
            {'name': 'Erick K', 'age': 31},
            {'name': 'Dickson K', 'age': 45},
            {'name': 'Earl M', 'age': 36},
            {'name': 'Sidra O', 'age': 27},
            {'name': 'James O', 'age': 29},
        ]

        for travel_companion_data in travel_companions_data:
            travel_companion = TravelCompanion(**travel_companion_data)
            db.add(travel_companion)

        
        # Seed Itineraries
        itineraries_data = [
            {'name': 'Adventure in Serengeti', 'user_id': 1},
            {'name': 'Exploring Victoria Falls', 'user_id': 2},
            {'name': 'Cultural Trip to Marrakech', 'user_id': 3},
            {'name': 'Hiking Table Mountain', 'user_id': 4},
            {'name': 'Historical Tour of Giza', 'user_id': 5},
            {'name': 'Summiting Kilimanjaro', 'user_id': 6},
            {'name': 'Safari in Okavango Delta', 'user_id': 7},
            {'name': 'Journey to Timbuktu', 'user_id': 8},
            {'name': 'Desert Expedition in Namib', 'user_id': 9},
            {'name': 'Wildlife Safari in Maasai Mara', 'user_id': 10},
        ]

        for itinerary_data in itineraries_data:
            itinerary = Itinerary(**itinerary_data)
            db.add(itinerary)


        # Seed Activities
        activities_data = [
            {'name': 'Safari'},
            {'name': 'Hiking'},
            {'name': 'Cultural Tour'},
            {'name': 'Historical Exploration'},
            {'name': 'Summiting'},
            {'name': 'Desert Expedition'},
            {'name': 'Wildlife Safari'},
        ]

        for activity_data in activities_data:
            activity = Activity(**activity_data)
            db.add(activity)



        # Seed Itinerary Items
        itinerary_items_data = [
            {'name': 'Game Drive in Serengeti', 'activity_id': 1, 'itinerary_id': 1},
            {'name': 'Visit to the Falls', 'activity_id': 2, 'itinerary_id': 2},
            {'name': 'Exploring Souks', 'activity_id': 3, 'itinerary_id': 3},
            {'name': 'Hike to the Summit', 'activity_id': 4, 'itinerary_id': 4},
            {'name': 'Tour of Pyramids', 'activity_id': 5, 'itinerary_id': 5},
            {'name': 'Climbing Kilimanjaro', 'activity_id': 6, 'itinerary_id': 6},
            {'name': 'Safari in Okavango Delta', 'activity_id': 1, 'itinerary_id': 7},
            {'name': 'Exploring Timbuktu', 'activity_id': 2, 'itinerary_id': 8},
            {'name': 'Desert Adventure', 'activity_id': 6, 'itinerary_id': 9},
            {'name': 'Wildlife Viewing', 'activity_id': 1, 'itinerary_id': 10},
        ]

        for itinerary_item_data in itinerary_items_data:
            itinerary_item = ItineraryItem(**itinerary_item_data)
            db.add(itinerary_item)

        # Commit the changes
        db.commit()

    finally:
        # Close the database session
        db.close()

if __name__ == "__main__":
    seed_data()
    print("Data has been seeded successfully.")
