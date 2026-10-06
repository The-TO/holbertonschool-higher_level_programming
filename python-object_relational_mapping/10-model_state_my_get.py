#!/usr/bin/python3
"""Prints the id of the State object whose name is passed as argument."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (session.query(State)
             .filter(State.name == sys.argv[4])
             .order_by(State.id)
             .first())

    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
