from models import Base, engine

def drop_and_create_database():
    # Drop the existing database (this will delete all data)
    Base.metadata.drop_all(bind=engine)

    # Create the database with tables
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    drop_and_create_database()
