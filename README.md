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

#### Register a New User

    ```bash

    python cli.py register
