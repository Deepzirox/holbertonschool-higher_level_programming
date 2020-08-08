from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
