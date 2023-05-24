#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ as env
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: table name
        name: input name
        cities: relation to cities table
    """
    __tablename__ = "states"

    if env.get('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            """get all cities with the current state id
            from filestorage
            """
            cities = [
                v for k, v in models.storage.all(models.City).items()
                if v.state_id == self.id
            ]
            return cities
