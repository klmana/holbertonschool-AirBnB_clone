#!/usr/bin/python3
"""
  File Storage
"""
import os
import json

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
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialzes __objects to JSON file.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """
        Deserializes the JSON file into __objects.
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            new_dict = json.load(f)
