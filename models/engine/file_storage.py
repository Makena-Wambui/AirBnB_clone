#!/usr/bin/python3

"""
This is the file_storage module.
It supplies one class: FileStorage
"""

from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage():
    """
    Class: FileStorage
    Serializes instances to a JSON file and deserializes JSON file to instances

    Private class attributes:
        __file_path => path to the JSON file
        __objects => an empty dictionary;
        will store all objects;

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public Instance Method: all

        Returns the dictionary, __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Public instance method: new

        Sets in the dict __objects the obj using key as objectsclassname plus
        objects id ex BaseModel.id
        """
        name = obj.__class__.__name__

        FileStorage.__objects[f"{name}.{obj.id}"] = obj

    def save(self):
        """
        Public instance method: save
        serializes __objects to the JSON file.
        """
        dict1 = FileStorage.__objects

        # Each key in dict1 represents an object.
        # lets use the dict method keys() to access these keys
        dict2 = {insta: dict1[insta].to_dict() for insta in dict1.keys()}

        # open the file for dumping
        file = FileStorage.__file_path
        with open(file, mode='w', encoding='utf-8') as f:
            json.dump(dict2, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        If the file doesn’t exist, no exception should be raised.
        """
        try:
            # let us open the json file.
            file = FileStorage.__file_path
            with open(file, encoding='utf-8') as f:
                dict1 = json.load(f)

            # now lets focus on the values of this dictionary only;
            # these values are dictionaries of instance attributes.

            for value in dict1.values():
                # extract classname to recreate our object with new method.

                name = value["__class__"]

                # we cannot create objects using the class name as a string
                # We need to convert it to an object using eval
                name = eval(name)

                # delete the __class__ key because our objects dont have it

                del value["__class__"]
                # recreate our objects using new
                self.new(name(**value))
        except FileNotFoundError:
            pass
