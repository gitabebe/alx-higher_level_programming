#!/usr/bin/python3
"""Defines a class City and an instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """links to the MySQL table cities

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        id (sqlalchemy.Integer): The city's id.
        name (sqlalchemy.String): The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
