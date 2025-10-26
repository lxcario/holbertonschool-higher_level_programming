#!/usr/bin/python3
"""Module for fetching city by state"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State
from sys import argv

# Run only when executed
if __name__ == "__main__":

    # Engine creation with mysql and mysqldb DBAPI
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    # Creating all classes in DB
    Base.metadata.create_all(engine)

    # Creating Session and its instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # The Query
    query = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all())

    # Printing the result
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Closing the session
    if session:
        session.close()
