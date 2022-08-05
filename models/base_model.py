#!/usr/bin/python3
"""
Base Model for AirBnB clone
"""


import uuid
from datetime import datetime


class BaseModel():
    """Base Model for AirBnB clone"""
    def __init__(self):
        """Initialize instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """str representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def save(self):
        """Updates time given change"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Create dictionary representation of the instance

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
