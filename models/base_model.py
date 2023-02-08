#!/usr/bin/python3

"""
This module defines a BaseModel class that defines
all common atttributes/methods for other classes
"""


import uuid
from datetime import datetime


class BaseModel():
    """
    A BaseModel class that defines all common methods
    and attributes for other classes
    """
    
    def __init__(self, *args, **kwargs):
        """
        *args and **kwargs arguments for the BaseModel
        if kwargs is not empty:
        each key of this dictionary is an attribute name
        (Note __class__ from kwargs is the only one
        that should not be added as an attribute
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        '''
        Returns a string representation of the base class
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute [update_at] with
        the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary representation of the BaseModel class
        """
        dct = self.__dict__.copy()
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.created_at.isoformat()
        dct["updated_at"] = self.updated_at.isoformat()
        return dct
