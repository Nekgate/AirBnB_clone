#!/usr/bin/python3
"""This module defines tests for User class"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test for user class"""

    def setUp(clas):
        """Sets up the user class"""
        clas.user = User()
        clas.user.email = "test@example.com"
        clas.user.password = "123456"
        clas.user.first_name = "Betty"
        clas.user.last_name = "Smith"

    def test_for_instantiation(self):
        """This tests for instatiation class User"""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_no_args_instantiates(self):
        """Tests for no args"""
        self.assertEqual(User, type(User()))

    def test_id_is_public_str(self):
        """Test id is a public string"""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Tests created at is public instance"""
        self.assertEqual(datetime, type(User().created_at))

    def test_has_attributes(self):
        """Tests the attributes"""
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_attributes_are_string(self):
        """Tests if attributes are strings"""
        self.assertIs(type(self.user.email), str)
        self.assertIs(type(self.user.password), str)
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.last_name), str)

    def test_is_subclass(self):
        """TestsnUser is a subclass of the BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email_attr(self):
        """Tests user email"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password_attr(self):
        """Tests for password"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        """Tests for first name"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Tests for last name"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """Tests for string method is correctly set"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def tests_is_subclass(self):
        """Tests if subclass"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel))

    def checking_for_doc(self):
        """Checks for docs"""
        self.assertIsNotNone(User.__doc__)

    def test_save(self):
        """Test save"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Tests dictionary"""
        self.assertTrue('to_dict' in dir(self.user))

    def test_to_dict_create_dict(self):
        """Tests to dict method"""
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test values in dict returned from to_dict are correct"""
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(dt_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(dt_format))


if __name__ == '__main__':
    unittest.main()
