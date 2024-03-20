#!/usr/bin/python3

"""
This is the user module.

It supplies one class: User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class: User

    A subclass of BaseModel

    Public Class Attributes:
        email
        password
        first_name
        last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
