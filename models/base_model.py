#!/usr/bin/python3

'''
This module defines a BaseModel class that defines
all common atttributes/methods for other classes
'''


import uuid
import datetime

class BaseModel():
    '''
    A BaseModel class that defines all common methods
    and attributes for other classes
    '''

    def __init__(self):
        '''
        creates a new instance of the BaseModel class
        '''
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        '''
        Returns a string representation of the base class
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attribute [update_at] with
        the current datetime
        '''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''
        returns a dictionary representation of the BaseModel class
        '''
        dct = {}
        
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dct[key] = value.isoformat()
            else:
                dct[key] = value
        dct['__class__'] = self.__class__.__name__
        
        return dct
