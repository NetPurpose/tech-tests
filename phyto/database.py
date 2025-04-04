from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy_utils.functions import database_exists, create_database, drop_database


def get_db_url(db_name: str = "phyto_db") -> str:
    return f"postgresql://postgres:postgres@localhost/{db_name}"


engine = create_engine(get_db_url())

# This is a an sqlalchemy session for interacting with the db
# https://docs.sqlalchemy.org/en/20/orm/session_api.html#session-api
Session = sessionmaker(engine)


# Use this to define ORM models of your database:
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html#declare-models
Base = declarative_base()


# Define models using Base above


if __name__ == "__main__":
    # Runnig this file as a module will result in the database being dropped and recreated.
    # Any models defined in Base will be created as tables.
    db_url = get_db_url()
    if database_exists(db_url):
        print(f"Dropping database {db_url}")
        drop_database(db_url)
    print(f"Creating database {db_url}")
    create_database(db_url)
    Base.metadata.create_all(engine)
