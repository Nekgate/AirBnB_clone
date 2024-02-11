#!/usr/bin/python3
"""This model defines the class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """The class user inherits from the base model"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
