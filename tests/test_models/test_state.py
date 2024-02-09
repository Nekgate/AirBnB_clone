#!/usr/bin/python3
"""This module defines tests for class state"""

import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """This tests for Class State"""

    def setUp(self):
        """Sets up the state class"""
        self.state = State()

    def test_attribute_initialization(self):
        """Tests whether class initializes"""
        self.assertEqual(self.state.name, "")

    def test_attribute_types(self):
        """Tests whether attr name is a string"""
        self.assertIsInstance(self.state.name, str)

    def test_attribute_values(self):
        """Tests whether values are coreectly set"""
        self.state.name = "Lagos"

        self.assertEqual(self.state.name, "Lagos")

    def test_update_attribute_values(self):
        """Tests whether values updated correctly"""
        self.state.name = "Nairobi"

        self.assertEqual(self.state.name, "Nairobi")


if __name__ == '__main__':
    unittest.main()
