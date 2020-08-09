#!/usr/bin/python3

'''
Get all states using sql alchemy
'''

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    lousiana = State(name='Louisiana')
    session.add(lousiana)
    id_number = session.query(State).filter_by(name="Louisiana").first()
    print(id_number.id)
    session.commit()
    session.close()
