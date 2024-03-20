#!/usr/bin/python3

"""
This is the review module.
Supplies one class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class: Review

    A subclass of BaseModel.

    Attribute = place_id -> Place.id
                user_id -> User.id
                text -> the review
    """

    place_id = ""
    user_id = ""
    text = ""
