#!/usr/bin/python3
"""This model describes the review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The model inherits from the base model"""
    place_id = ""
    user_id = ""
    text = ""
