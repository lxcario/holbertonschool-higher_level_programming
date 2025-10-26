#!/usr/bin/python3
"""
Module for fetching first state from the database using SQLAlchemy ORM.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

from model_state import Base, State

# Run only executed
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
    state = session.query(State).order_by(State.id).first()

    # Printing the result
    if state is None:
        print("Nothing")
    else:
        print("1: {}".format(state.name))

    # Closing the session
    if session:
        session.close()
