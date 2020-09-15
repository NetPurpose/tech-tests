from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.functions import database_exists, create_database


def get_db_url(db_name="phyto_db"):
    return f"postgresql://postgres:postgres@localhost/{db_name}"


engine = create_engine(get_db_url())
# This is a an sqlalchemy session for interacting with the db
# https://docs.sqlalchemy.org/en/13/orm/session.html
Session = sessionmaker(engine)

# Use this to define ORM models of your database:
# https://docs.sqlalchemy.org/en/13/orm/
Base = declarative_base()

if __name__ == "__main__":
    if not database_exists(get_db_url()):
        create_database(get_db_url())
    Base.metadata.create_all(engine)
