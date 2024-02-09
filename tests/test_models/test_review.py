#!/usr/bin/python3
"""This module defines tests for class review"""

import unittest
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """Tests for class review"""

    def setUp(self):
        """Sets up the class review"""
        self.review = Review()

    def test_attribute_initialization(self):
        """Test for initialization of attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attribute_values(self):
        """Tests whether values are correctly set"""
        self.review.place_id = "412"
        self.review.user_id = "420"
        self.review.text = "5 star!"

        self.assertEqual(self.review.place_id, "412")
        self.assertEqual(self.review.user_id, "420")
        self.assertEqual(self.review.text, "5 star!")

    def test_update_attribute_values(self):
        """Tests whether values updates as expected"""
        self.review.place_id = "413"
        self.review.user_id = "421"
        self.review.text = "5 star! Awesome place"

        self.assertEqual(self.review.place_id, "413")
        self.assertEqual(self.review.user_id, "421")
        self.assertEqual(self.review.text, "5 star! Awesome place")


if __name__ == '__main__':
    unittest.main()
