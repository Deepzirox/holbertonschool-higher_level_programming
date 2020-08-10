#!/usr/bin/python3

'''
Get all states using sql alchemy
'''

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base as base_state, State
from model_city import Base as base_city, City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).all():
        print("{}: {}".format(state.id, state.name))
        for city in session.query(City).filter(state.id == City.state_id):
            print("\t{}: {}".format(city.id, city.name))

    session.close()
