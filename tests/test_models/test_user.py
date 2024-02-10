#!/usr/bin/python3
"""This module defines tests for User class"""

import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Test for user class"""

    def setUp(self):
        """Sets up the user class"""
        self.user = User()

    def test_init(self):
        """Initializes the user class"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_attributes(self):
        """Tests the attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_creation(self):
        """Tests the set values for attributes"""
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_to_dict(self):
        """Tests set dictionary for user"""
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'test@example.com')
        self.assertEqual(user_dict['password'], 'password')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')

    def test_user_from_dict(self):
        """Tests collection of data from the dictionary"""
        user_data = {
            '__class__': 'User',
            'id': '412',
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**user_data)
        self.assertEqual(user.id, '412')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')


if __name__ == '__main__':
    unittest.main()
