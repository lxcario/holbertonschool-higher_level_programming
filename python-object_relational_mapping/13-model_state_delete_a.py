#!/usr/bin/python3
"""
Module for deleting all the cities with 'a'.
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

    # Deleting everything with a
    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    session.commit()

    # Closing the session
    if session:
        session.close()
