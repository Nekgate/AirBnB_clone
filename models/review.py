#!/usr/bin/python3
"""This model describes the class review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The class review inherits from the base model"""
    place_id = ""
    user_id = ""
    text = ""
