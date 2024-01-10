from faker import Faker
import csv

fake = Faker()

# Sample User Data
users_data = [{'username': fake.user_name(), 'email': fake.email()} for _ in range(10)]

# Sample Destination Data
destinations_data = [{'name': fake.word(), 'location': fake.city()} for _ in range(5)]

# Sample Activity Data
activities_data = [{'name': fake.word(), 'description': fake.sentence()} for _ in range(8)]

# Sample Travel Companion Data
travel_companions_data = [
    {'name': fake.name(), 'age': fake.random_int(min=18, max=60), 'gender': fake.random_element(elements=('Male', 'Female'))}
    for _ in range(6)
]

# Save to CSV
with open('sample_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['username', 'email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users_data)

    fieldnames = ['name', 'location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(destinations_data)

    fieldnames = ['name', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(activities_data)

    fieldnames = ['name', 'age', 'gender']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(travel_companions_data)
