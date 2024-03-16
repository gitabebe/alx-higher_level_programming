#!/usr/bin/python3
"""prints the State object with the name passed as argument from database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    state = session.query(State).filter(State.name == argv[4]).first()
    if state is None:
        print('Not found')
    else:
        print('{0}'.format(state.id))
    session.close()
