#!/usr/bin/python3
"""
  File Storage
"""

from os.path import exists
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

classes = {"BaseModel": BaseModel, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review, "User": User}


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
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    def save(self):
        """
        Serialzes __objects to JSON file.
        """
        j_objects = {}
        for k in self.__objects:
            j_objects[k] = self.__objects[k].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(j_objects, f)

    def reload(self):
        """
        Deserializes the JSON file into __objects.
        """
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                j = json.load(f)
                for k in j:
                    self.__objects[k] = classes[j[k]["__class__"]](**j[k])
