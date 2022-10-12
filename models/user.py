#!/usr/bin/python3
"""
  The User class.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Constructs a User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, *kwargs):
        """Initialisation of user"""
        super().__init__(*args, **kwargs)
