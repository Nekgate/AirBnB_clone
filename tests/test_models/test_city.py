#!/usr/bin/python3
"""This module defines tests for class city"""

import unittest
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """This tests for class City"""

    def setUp(self):
        """sets up ths city class"""
        self.city = City()

    def test_attribute_initialization(self):
        """Tests whether attributes are correcrtly put"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_attribute_types(self):
        """Tests for correct attributes"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_attribute_values(self):
        """Tests set values for attributes"""
        self.city.state_id = "476"
        self.city.name = "Lagos"

        self.assertEqual(self.city.state_id, "476")
        self.assertEqual(self.city.name, "Lagos")

    def test_update_attribute_values(self):
        """Test for update values"""
        self.city.name = "Nairobi"

        self.assertEqual(self.city.name, "Nairobi")


if __name__ == '__main__':
    unittest.main()
