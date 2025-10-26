#!/usr/bin/python3
"""
Module for adding Louisiana.
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

    # Creating new city instance and adding it do db
    s = State(name='Louisiana')
    session.add(s)
    session.commit()

    # Printing the new State id
    print(s.id)

    # Closing the session
    if session:
        session.close()
