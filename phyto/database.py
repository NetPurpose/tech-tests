from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.functions import database_exists, create_database, drop_database


def get_db_url(db_name="phyto_db"):
    return f"postgresql://postgres:postgres@localhost/{db_name}"


engine = create_engine(get_db_url())
# This is a an sqlalchemy session for interacting with the db
# https://docs.sqlalchemy.org/en/13/orm/session.html
Session = sessionmaker(engine)

# Use this to define ORM models of your database:
# https://docs.sqlalchemy.org/en/13/orm/
Base = declarative_base()


class LocalAuthority(Base):
    __tablename__ = "local_authorities"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True)
    sample_number = Column(String, nullable=False)
    bed_id = Column(String, nullable=True)
    local_authority_id = Column(
        Integer, ForeignKey(LocalAuthority.id, ondelete="CASCADE")
    )
    collection_method = Column(String, nullable=False)
    date_collected = Column(Date, nullable=False)
    date_arrived = Column(Date, nullable=False)
    date_analysed = Column(Date, nullable=False)

    alex = Column(Integer, nullable=True)
    gym = Column(Integer, nullable=True)
    dino = Column(Integer, nullable=True)
    pro = Column(Integer, nullable=True)
    pseudo = Column(Integer, nullable=True)
    karen = Column(Integer, nullable=True)
    yesso = Column(Integer, nullable=True)
    proto = Column(Integer, nullable=True)
    vener = Column(Integer, nullable=True)
    crass = Column(Integer, nullable=True)

    local_authority = relationship(LocalAuthority, backref="samples")


if __name__ == "__main__":
    drop_database(get_db_url())
    create_database(get_db_url())
    Base.metadata.create_all(engine)
