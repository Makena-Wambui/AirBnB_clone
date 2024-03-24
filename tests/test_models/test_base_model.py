#!/usr/bin/python3

"""
This module contains tests for the BaseModel class.
Tests all methods and attributes in this class.
"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelInstantiation(unittest.TestCase):
    """ Tests BaseModel Instantiation."""

    def test_no_args(self):
        """Tests BaseModel Instantiation"""
        object1 = BaseModel()
        self.assertEqual(BaseModel, type(object1))

    def test_id(self):
        """ Tests that id attribute is a string."""
        object2 = BaseModel()
        self.assertEqual(str, type(object2.id))

    def test_unique_ids(self):
        """ Tests if different objects have different ids."""
        object1 = BaseModel()
        object2 = BaseModel()
        self.assertNotEqual(object1.id, object2.id)

    def test_created_at(self):
        """ Test that created_at is a datetime object."""
        object3 = BaseModel()
        self.assertEqual(datetime, type(object3.created_at))

    def test_updated_at(self):
        """ Test that updated_at is a datetime object."""
        object4 = BaseModel()
        self.assertEqual(datetime, type(object4.created_at))

    def test_storage(self):
        """Test if created object is successfully stored in __objects."""
        objects = models.storage.all().values()
        object1 = BaseModel()
        self.assertIn(object1, objects)

    def test_two_objects_with_diff_created_at(self):
        """
        Test that two BaseModel objects have different values
        for the created_at attribute.
        """
        object1 = BaseModel()
        object2 = BaseModel()
        self.assertNotEqual(object1.created_at, object2.created_at)


if __name__ == "__main__":
    unittest.main()
