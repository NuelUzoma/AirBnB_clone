#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        returns the dictionary __objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Sets in [__objects] the obj with the key <obj classname>.id

        Args:
            obj - The object to add to the [__objects] class attribute
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        serializes [__object] to the JSON file
        '''
        dct = FileStorage.__objects
        objdict = {}

        for key, value in dct.items():
            objdict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objdict, file, indent=4)

    def reload(self):
        '''
        deserializes the JSON file to [__objects]
        '''
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objdict = json.load(file)
                for key, value in objdict.items():
                    objstr = value["__class__"]
                    obj = eval(objstr)(**value)
                    FileStorage.__objects[key] = obj
        except Exception:
            pass
