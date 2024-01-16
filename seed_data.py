from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Destination, Activity

engine = create_engine('sqlite:///tuelekee.db')
Base.metadata.bind = engine

#Session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

#Destinations and activities
destinations_data = [
    {
        'name': 'DIANI - KENYA',
        'activities': [
            {'name': 'Yoga & Fitness Retreats'},
            {'name': 'Kite Surfing Diani Beach'},
            {'name': 'Glass Bottom Boat & Snorkelling'},
            {'name': 'Colobus Monkey Sanctuary Visit'},
            {'name': 'Shimba Hills National Reserve Safari'},
        ]
    },
    {
        'name': 'CAPE TOWN - SOUTH AFRICA',
        'activities': [
            {'name': 'Table Mountain Hiking'},
            {'name': 'Robben Island Historical Tour'},
            {'name': 'Cape Winelands Wine Tasting'},
            {'name': 'Boulders Beach Penguin Colony Visit'},
            {'name': 'Kirstenbosch Botanical Gardens Exploration'},
        ]
    },
    {
        'name': 'MARRAKECH - MOROCCO',
        'activities': [
            {'name': 'Exploring Jardin Majorelle'},
            {'name': 'Shopping in the Medina'},
            {'name': 'Hot Air Balloon Ride over Atlas Mountains'},
            {'name': 'Traditional Moroccan Cooking Class'},
            {'name': 'Saadian Tombs Visit'},
        ]
    },
    {
        'name': 'VICTORIA FALLS - ZAMBIA/ZIMBABWE',
        'activities': [
            {'name': "Devil's Pool Swim (seasonal)"},
            {'name': 'Helicopter Flight over Victoria Falls'},
            {'name': 'White-water Rafting in the Zambezi River'},
            {'name': 'Elephant Back Safari'},
            {'name': 'Livingstone Island Tour'},
        ]
    },
    {
        'name': 'SERENGETI NATIONAL PARK - TANZANIA',
        'activities': [
            {'name': 'Great Migration Safari'},
            {'name': 'Hot Air Balloon Safari'},
            {'name': 'Olduvai Gorge Archaeological Site Visit'},
            {'name': 'Serengeti Cultural Tours'},
            {'name': 'Bird Watching in Seronera Valley'},
        ]
    },
    {
        'name': 'MAASAI MARA NATIONAL RESERVE - KENYA',
        'activities': [
            {'name': 'Maasai Village Cultural Experience'},
            {'name': 'Hot Air Balloon Safari'},
            {'name': 'Great Migration Safari'},
            {'name': 'Nature Walks with Maasai Guides'},
            {'name': 'Photography Safaris'},
        ]
    },
    {
        'name': 'ZANZIBAR - TANZANIA',
        'activities': [
            {'name': 'Stone Town Historical Walking Tour'},
            {'name': 'Spice Farm Tour'},
            {'name': 'Snorkeling in Mnemba Atoll'},
            {'name': 'Jozani Chwaka Bay National Park Visit'},
            {'name': 'Sunset Dhow Cruise'},
        ]
    },
    {
        'name': 'KRUGER NATIONAL PARK - SOUTH AFRICA',
        'activities': [
            {'name': 'Big Five Safari'},
            {'name': 'Bushwalks with Experienced Guides'},
            {'name': 'Stargazing in the African Bush'},
            {'name': 'Visit to Blyde River Canyon'},
            {'name': "Pilgrim's Rest Historical Village Exploration"},
        ]
    },
    {
        'name': 'NAMIB DESERT - NAMIBIA',
        'activities': [
            {'name': 'Sossusvlei Dune Climbing'},
            {'name': 'Deadvlei Photography'},
            {'name': 'Hot Air Balloon Safari over the Desert'},
            {'name': 'Quad Biking in the Dunes'},
            {'name': 'Visit to Sesriem Canyon'},
        ]
    },
    {
        'name': 'CAIRO - EGYPT',
        'activities': [
            {'name': 'Giza Pyramids and Sphinx Tour'},
            {'name': 'Nile River Cruise'},
            {'name': 'Egyptian Museum Exploration'},
            {'name': 'Khan El Khalili Bazaar Shopping'},
            {'name': 'Islamic Cairo Walking Tour'},
        ]
    },
]

for destination_info in destinations_data:
    destination = Destination(name=destination_info['name'])
    session.add(destination)
    session.commit()

    for activity_info in destination_info['activities']:
        activity = Activity(name=activity_info['name'], destination=destination)
        session.add(activity)
        session.commit()

print("Data added to the database.")
