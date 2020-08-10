#!/usr/bin/python3

'''
Get all states using sql alchemy
'''

from sqlalchemy import (create_engine, func)
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base as base_state, State
from model_city import Base as base_city, City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(
        City, State).filter(
            City.state_id == State.id).order_by(State.id, City.id).all()
    curr = 0
    for ct, st in query:
        if st.name == curr:
            print("    {}: {}".format(ct.id, ct.name))
            continue
        else:
            print("{}: {}".format(st.id, st.name))
            curr = st.name
        print("    {}: {}".format(ct.id, ct.name))

    session.close()
