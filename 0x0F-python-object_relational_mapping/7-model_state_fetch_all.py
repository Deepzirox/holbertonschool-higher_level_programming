#!/usr/bin/python3
from sqlalchemy import (create_engine, MetaData, Table, select)
import sys
from model_state import Base, State

'''
Get all states using sql alchemy
'''

def db_connect():
    '''
        Connection to DB and return all rows
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    conn = engine.connect()
    #Base.metadata.create_all(engine)
    states = Table('states', MetaData(), autoload=True, autoload_with=engine)
    query = select([states])
    proxy = conn.execute(query)
    return proxy.fetchall()

def print_result(result):
    '''
        print results from db_connect
    '''
    for row in result:
        print("{}. {}".format(row[0], row[1]))

if __name__ == "__main__":
    print_result(db_connect())
