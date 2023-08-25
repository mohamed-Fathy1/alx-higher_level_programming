#!/usr/bin/python3
'''
Write a python file that contains the class definition of
a State and an instance Base = declarative_base()
'''
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    ''' city class'''
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
