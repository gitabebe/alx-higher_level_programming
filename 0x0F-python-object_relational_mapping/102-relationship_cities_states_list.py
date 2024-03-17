#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(State).join(City).order_by(City.id).all()
    for state in st:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
