#!/usr/bin/python3
"""This module contains the Class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """The user model inherits from the base model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
