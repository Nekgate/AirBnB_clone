#!/usr/bin/python3
"""This model defines the class place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """The class place inherits from base model"""
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
