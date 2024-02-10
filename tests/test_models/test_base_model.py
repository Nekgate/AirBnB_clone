#!/usr/bin/python3
"""This defines the test module for base_model"""

import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel"""

    def test_init(self):
        """Tests iniatialization of the attributes"""
        mod = BaseModel()

        self.assertIsNotNone(mod.id)
        self.assertIsNotNone(mod.created_at)
        self.assertIsNotNone(mod.updated_at)

    def test_save(self):
        """Tests to confirm the method works as expected"""
        mod = BaseModel()

        initial_updated_at = mod.updated_at

        current_updated_at = mod.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """Tests that the dictionary contains all expected attributes"""
        mod = BaseModel()

        mod_dict = mod.to_dict()

        self.assertIsInstance(mod_dict, dict)

        self.assertEqual(mod_dict['id'], mod.id)
        self.assertEqual(mod_dict["__class__"], 'BaseModel')
        self.assertEqual(mod_dict['created_at'], mod.created_at.isoformat())
        self.assertEqual(mod_dict['updated_at'], mod.updated_at.isoformat())

    def test_str(self):
        """Tests for the string method"""
        mod = BaseModel()

        self.assertTrue(str(mod).startswith('[BaseModel]'))

        self.assertIn(mod.id, str(mod))

        self.assertIn(str(mod.__dict__), str(mod))


if __name__ == '__main__':
    unittest.main()
