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
import models
FileStorage = file_storage.FileStorage


class TestDocsFileStorage(unittest.TestCase):
    """Tests for the FileStorage's docs."""

    @classmethod
    def setUpClass(cls):
        """Sets up the FileStorage class."""
        cls.base_funcs = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions."""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """Checks pycodestyle for file storage."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """Checks pycodestyle for test_file_storage."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
