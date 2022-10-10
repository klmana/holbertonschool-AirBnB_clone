#!/usr/bin/python3
"""
  File Storage
"""

from os.path import exists
import json
from models.base_model import BaseModel


class FileStorage:

    """
    That serializes instances to a JSON file
    and deserializes JSON file to instance
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the  __objects dictionary.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialzes __objects to JSON file.
        """
        j_objects = {}
        for key in self.__objects:
            j_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(j_objects, f)

    def reload(self):
        """
        Deserializes the JSON file into __objects.
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                j_objects = json.load(f)
                for key in j_objects:
                    self.__objects[key] = BaseModel(**j_objects[key])
