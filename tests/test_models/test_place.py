#!/usr/bin/python3
"""This module defines tests for class place"""

import unittest
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """Tests for the class Place"""

    def setUp(self):
        """Sets up class Place"""
        self.place = Place()

    def test_attribute_initialization(self):
        """Tests if attributes are initialized"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_types(self):
        """Tests whether attributes are correct"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_attribute_values(self):
        """This tests values are correctly set"""

        self.place.city_id = "424"
        self.place.user_id = "421"
        self.place.name = "Example Place"
        self.place.description = "This is an example place"
        self.place.number_rooms = 4
        self.place.number_bathrooms = 2
        self.place.max_guest = 8
        self.place.price_by_night = 1500
        self.place.latitude = 26.4587
        self.place.longitude = 80.3698
        self.place.amenity_ids = ["WIFI", "PARKING"]

        self.assertEqual(self.place.city_id, "424")
        self.assertEqual(self.place.user_id, "421")
        self.assertEqual(self.place.name, "Example Place")
        self.assertEqual(self.place.description, "This is an example place")
        self.assertEqual(self.place.number_rooms, 4)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 8)
        self.assertEqual(self.place.price_by_night, 1500)
        self.assertEqual(self.place.latitude, 26.4587)
        self.assertEqual(self.place.longitude, 80.3698)
        self.assertEqual(self.place.amenity_ids, ["WIFI", "PARKING"])

    def test_update_attribute_values(self):
        """Tests whether values can be updated"""
        self.place.name = "Updated Name"
        self.place.number_rooms = 5
        self.place.price_by_night = 2000

        self.assertEqual(self.place.name, "Updated Name")
        self.assertEqual(self.place.number_rooms, 5)
        self.assertEqual(self.place.price_by_night, 2000)

    def test_boundary_conditions(self):
        """Test the boundaries of the conditions"""
        self.place.number_rooms = 10000000
        self.place.price_by_night = 999999999
        self.place.latitude = 40.0
        self.place.longitude = 210.0

        self.assertEqual(self.place.number_rooms, 10000000)


if __name__ == '__main__':
    unittest.main()
