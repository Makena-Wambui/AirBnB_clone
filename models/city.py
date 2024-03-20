#!/usr/bin/python3

"""
This is the city module.
Supplies one class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class: City

    A subclass of BaseModel.

    Attribute = state_id: State.id
                name: city's name
    """

    state_id = ""
    name = ""
