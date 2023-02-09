#!/usr/bin/python3

'''
This module contains the FileStorage class
'''


import json
from models.base_model import BaseModel


class FileStorage():
    '''
    FileStorage class that serializes and deserializes python objects
    '''
    
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
        
        args:
            obj - The object to add to the [__objects] class attribute
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        serializes [__object] to the JSON file
        '''
        dict = FileStorage.__objects
        objdict = {}
        
        for key, value in dict.items():
            objdict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(objdict, file)

    def reload(self):
        '''
        deserializes the JSON file to [__objects]
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                file_content = file.read()
                objdict = json.loads(file_content)
                for value in objdict.values():
                    objstr = value["__class__"]
                    del value["__class__"]
                    self.new(eval(objstr)(**value))
        except:
            return