#!/usr/bin/python3

"""
This is the amenity module.
Supplies one class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class: Amenity

    A subclass of BaseModel.

    Attribute => name: name of amenity
    """

    name = ""
