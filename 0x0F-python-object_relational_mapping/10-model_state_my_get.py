#!/usr/bin/python3
"""prints the State object with the name passed
as argument from db hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).filter(State.name == sys.argv[4]).first()
    print("Not found" if not res else res.id)

    session.close()
