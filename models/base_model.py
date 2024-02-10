#!/usr/bin/python3
"""
This is the Base Model it defines all common
attributes for other classes.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class describes public instances"""
    def __init__(self, *args, **kwargs):
        """Initializes an instance"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                    continue

                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())

            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)

    def save(self):
        """
        Updates the instance attribute updated_at anytime the objected
        is changed
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Returns a readable string representation"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """Creates a copy of instance attributes and class name"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__

        for key, value in my_dict.items():
            if isinstance(value, datetime):
                my_dict[key] = value.isoformat()

        return my_dict
