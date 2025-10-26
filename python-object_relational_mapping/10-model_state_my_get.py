#!/usr/bin/python3
"""
Module for fetching all states containing letter 'a'.
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
    state = (session.query(State)
             .filter(State.name == argv[4])
             .first())

    # Printing the result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Closing the session
    if session:
        session.close()
