#!/usr/bin/python3
"""This module defines tests for file storage"""

import json
import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """File Storage tests"""

    def setUp(self):
        """The instance of filestorage used"""
        self.file_storage = FileStorage()

    def test_init(self):
        """Confirms whether object empty and path set the correct way"""
        self.assertEqual(self.file_storage._FileStorage__objects, {})

        self.assertEqual(
            self.file_storage._FileStorage__file_path, "file.json")

    def test_all(self):
        """Test all function works as expected"""
        self.assertEqual(self.file_storage.all(), {})

        mod1 = BaseModel()
        mod2 = BaseModel()
        self.file_storage.new(mod1)
        self.file_storage.new(mod2)
        expected_dict = {
            'BaseModel.' + mod1.id: mod1.to_dict(),
            'BaseModel.' + mod2.id: mod2.to_dict()
        }
        self.assertEqual(self.file_storage.all(), expected_dict)

    def test_new(self):
        """Tests the new method adds to objects"""
        mod = BaseModel()
        self.file_storage.new(mod)

        expected_key = 'BaseModel.' + mod.id
        self.assertIn(expected_key, self.file_storage._FileStorage__objects)
        self.assertEqual(self.file_storage._FileStorage__objects[expected_key],
                         mod.to_dict())

    def test_save(self):
        """Tests the save method"""
        mod1 = BaseModel()
        mod2 = BaseModel()
        self.file_storage.new(mod1)
        self.file_storage.new(mod2)

        self.file_storage.save()

        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", "r") as f:
            data = json.load(f)
            expected_data = {
                'BaseModel.' + mod1.id: mod1.to_dict(),
                'BaseModel.' + mod2.id: mod2.to_dict()
            }
            self.assertEqual(data, expected_data)

        def test_reload(self):
            """Tests reload method"""
            data = {
                'BaseModel.412': {'id': '412', 'name': 'object1'},
                'BaseModel.413': {'id': '413', 'name': 'object2'}
            }
            with open("file.json", "w") as f:
                json.dump(data, f)

            self.file_storage._FileStorage__objects = {}

            self.file_storage.reload()

            self.assertEqual(self.file_storage._FileStorage__objects, data)


if __name__ == '__main__':
    unittest.main()
