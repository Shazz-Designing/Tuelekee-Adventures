# Tuelekee Adventures

## Project Description

Tuelekee Adventures is a Python-based Command-Line Interface (CLI) application designed to simplify travel itinerary management. The CLI enables users to register, explore destinations, view and create travel itineraries, and manage various aspects of their adventures. The project incorporates SQLAlchemy ORM for efficient database interactions, creating a seamless experience for users seeking to plan and organize their travels.

## TABLE OF CONTENTS

- [Installation](#installation)
- [Usage](#usage)
- [Key Features](#key-features)
- [Database Schema](#database-schema)
- [Virtual Environment](#virtual-environment)
- [Acknowledgments](#acknowledgments)
- [Project Requirements](#project-requirements)
- [Learning Goals](#learning-goals)

## INSTALLATION

To run Tuelekee Adventures, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Shazz-Designing/Tuelekee-Adventures.git

2. Navigate to the project directory:

    ```bash

   cd tuelekee-adventures

3. Install dependencies using Pipenv:

    ```bash

    pipenv install

4. Create and initialize the database: 

    ```bash

    alembic upgrade head


## USAGE

### User Management

1. Register a New User

    ```bash

    python cli.py register


Follow the prompts to enter the user's information.


2. View User Details
    
    ```bash

    python cli.py view_user <user_id>

Replace <user_id> with the ID of the user you want to view.

3. List All Users

   ```bash

    python cli.py list_users

4. Activity Management        

        ```bash

        python cli.py view_activity <activity_id>

        python cli.py list_activities

5. Destination Exploration

        ```bash

        python cli.py list_destinations

6. Itinerary Creation
    
        ```bash

        python cli.py create_itinerary <user_id>

Follow the prompts to select a destination, activities, and specify if a travel companion is desired. Replace <user_id> with the ID of the user for whom the itinerary is created.

## KEY FEATURES
### User Management: Register new users, view user details, and list all users in the database.

### Activity Management: View details of specific activities, list all activities, and explore destinations and their associated activities.

### Destination Exploration: List all destinations and their activities, allowing users to choose from a variety of options.

### Itinerary Creation: Create travel itineraries by selecting a user, destination, activities, and specifying if a travel companion is desired.


## DATABASE SCHEMA
The project employs a well-designed database schema using SQLAlchemy ORM. The schema includes tables for users, activities, destinations, and itineraries, establishing one-to-many and many-to-many relationships where necessary.

## Tables
users: Stores user information, including name, email, and age.

activities: Represents various activities available at different destinations.

destinations: Contains information about travel destinations and their associated activities.

itineraries: Records travel itineraries, linking users, destinations, and selected activities.

## Relationships
User-Itinerary Relationship (One-to-Many):

A user can have multiple itineraries.
An itinerary belongs to one user.
Destination-Activity Relationship (One-to-Many):

A destination can have multiple activities.
An activity belongs to one destination.
Itinerary-Activity Relationship (Many-to-Many):

An itinerary can have multiple activities.
An activity can be associated with multiple itineraries.

## VIRTUAL ENVIRONMENT
1. The project utilizes Pipenv to maintain a well-structured virtual environment. Ensure that the virtual environment is activated before running any CLI commands.
     
        ```bash

    pipenv shell

## Contributing
If you'd like to contribute, please fork the repository and create a new branch. Pull requests are welcome!

## License
This project is licensed under the MIT License.
