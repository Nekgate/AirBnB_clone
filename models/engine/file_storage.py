#!/usr/bin/python3
"""This module contains the class FileStorage"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    file storage class is responsible for serialization of instances to JSON
    and deserialization of JSON to instances
    """

    def __init__(self):
        """Init an instance and sets the values for private properties"""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary of objects"""

        return self.__objects

    def new(self, obj):
        """Sets new obj in __objects in the dictionary."""

        name = obj.__class__.__name__ + "." + obj.id
        self.__objects[name] = obj.to_dict()
        self.save()

    def save(self):
        """Serializes __objects to the JSON file __file_path."""

        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "Amenity": Amenity,
            "City": City,
            "Review": Review,
            "State": State
        }

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
