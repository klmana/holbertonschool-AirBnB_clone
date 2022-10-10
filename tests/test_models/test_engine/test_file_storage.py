#!/usr/bin/python3
"""
Unittest module for the FileStorage class.
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """
    Test Cases for the FileStorage class.
    """

    def setUp(self):
        """
        Sets up test methods.
        """
        pass
