#!/usr/bin/python3
from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

'''
New states object model
'''

Base = declarative_base()


class State(Base):
    '''
        Class that inherit from base
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
