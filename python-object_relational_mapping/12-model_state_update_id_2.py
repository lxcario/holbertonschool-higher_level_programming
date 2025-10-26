#!/usr/bin/python3
"""
Module for New Mexico update.
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

    # Changing state name to New Mexico
    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})
    session.commit()

    # Closing the session
    if session:
        session.close()
