#!/usr/bin/python3
"""
Base Model for AirBnB clone
"""


import uuid
from datetime import datetime

format_dt = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """Base Model for AirBnB clone"""
    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_dt)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
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
