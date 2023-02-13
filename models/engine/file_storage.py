#!/usr/bin/python3
"""
Class that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """ Class that serializes and deserializes JSON objects """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name >.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dictionary = {}

        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(dictionary, f, indent=4)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User

        dct = {'BaseModel': BaseModel, 'User': User}


        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))
