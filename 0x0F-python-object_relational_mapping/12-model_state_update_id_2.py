#!/usr/bin/python3
"""Start link class to table in database
"""
from os import name
import sys

from sqlalchemy.orm import Session
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(State).filter_by(id=2)
    if query:
        for row in query:
            row.name = 'New Mexico'
    session.commit()
