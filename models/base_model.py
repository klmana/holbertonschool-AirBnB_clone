#!/usr/bin/python3
"""
Module containing "Base" class.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The base model class.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructs a BaseModel class.
        """
        dateformat = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dateformat)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of BaseModel
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates public instance attribute updated_at
        with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__
        """
        new_dict = {}
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
