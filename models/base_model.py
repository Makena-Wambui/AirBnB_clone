#!/usr/bin/python3

"""
This is the base_model module.
It supplies one class: BaseModel
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Class: BaseModel
    Defines all common attributes/methods for other classes

    Public instance attributes:
        id => unique id for each object
        created_at => current datetime when an instance is created
        updated_at => current datetime when an instance is created;
        and updated every time you change your object

    Methods:
        __init__
        __str__
        save
        to_dict
    """
    def __init__(self, *args, **kwargs):
        """
        Class Constructor __init__.

        Automatically called each time we instantiate BaseModel.

        """
        formatt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # if kwargs is not empty
        if len(kwargs) != 0:
            new_dict = {k: v for k, v in kwargs.items() if k != "__class__"}

            for k, v in new_dict.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, formatt)
                    self.__dict__[k] = v
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns an informal string representation of an object.
        """
        name = self.__class__.__name__
        obj_id = self.id
        obj_d = self.__dict__
        return "[{}] ({}) {}".format(name, obj_id, obj_d)

    def save(self):
        """
        Updates the instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        # make a copy of self.__dict__
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
