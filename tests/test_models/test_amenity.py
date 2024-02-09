#!/usr/bin/python3
"""This module test for class amenity"""

import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Tests the class amenity"""

    def setUp(self):
        """sets up the class amenity"""
        self.amenity = Amenity()

    def tets_attribute_initialization(self):
        """Tests for initialization of amenity attributes"""
        self.assertEqual(self.amenity.name, "")

    def test_attribute_types(self):
        """Tests for attributes"""
        self.assertIsInstance(self.amenity.name, str)

    def test_attribute_values(self):
        """Tests for set attribute values"""
        self.amenity.name = "WIFI"

        self.assertEqual(self.amenity.name, "WIFI")

    def test_update_attribute_values(self):
        """Tests the updated attribute values"""
        self.amenity.name = "PARKING"

        self.assertEqual(self.amenity.name, "PARKING")


if __name__ == '__main__':
    unittest.main()
