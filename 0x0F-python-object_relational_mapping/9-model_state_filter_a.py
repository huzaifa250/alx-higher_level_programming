#!/usr/bin/python3
"""Lists all State objects that contain the letter a from the database"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).filter(State.name.like('%a%')).all()

    for state in res:
        print("{}: {}".format(state.id, state.name))
