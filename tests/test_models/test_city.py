#!/usr/bin/python3
"""Unit test for city Class
"""

import unittest
from models.city import City
from models.base_model import BaseModel
import os


class TestCityClass(unittest.TestCase):
    """Tests City class"""

    def setUp(self):
        """init for  each test"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_docs(self):
        """ check documentation """
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test inheritance of BaseModel """
        my_user = City()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_field_types(self):
        """ Test type of attributes """
        my_user = City()
        self.assertTrue(type(my_user.name) == str)


if __name__ == '__main__':
    unittest.main()
