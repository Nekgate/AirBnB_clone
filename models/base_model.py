#!/usr/bin/python3
"""
This is our base model defines all common
attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for all other models"""

    def __init__(self, *args, **kwargs):
        """initialize an instance"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                    continue

                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the public instance atrribute updated_at whenever changed"""

        self.updated_at = datetime.now()
        storage.save()

    def __str__(sef):
        """Returns a readable string representation of BaseModel instances"""

        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """Creates a copy of instance attributes"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        for key, value in obj_dict.items():
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()

        return obj_dict
