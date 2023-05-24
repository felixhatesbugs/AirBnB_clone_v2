#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        __tablename__: name of the table represented
        state_id: The state id
        name: input name
    """

    __tablename__ = "cities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade="all, delete, delete-orphan",
                              backref="city")
    else:
        state_id = ""
        name = ""
