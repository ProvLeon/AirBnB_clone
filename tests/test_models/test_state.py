#!/usr/bin/python3
"""Unittest for amenity.py"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """Tests instances and methods from the State class"""

    s = State()

    def test_class_exists(self):
        """Tests if the class exists"""
        expected_type = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), expected_type)

    def test_user_inheritance(self):
        """Tests if State is a subclass of BaseModel"""
        self.assertIsInstance(self.s, State)

    def test_has_attributes(self):
        """Verifies if attributes exist"""
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_types(self):
        """Tests if the type of the attribute is correct"""
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()