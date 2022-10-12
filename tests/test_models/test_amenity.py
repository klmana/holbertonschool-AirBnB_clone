#!/usr/bin/python3
"""Contains tests for Amenity class."""

import pycodestyle
import unittest
import datetime
import uuid
import inspect

from models.base_model import BaseModel
from models.amenity import Amenity


class TestDocsAmenity(unittest.TestCase):
    """Tests for the Amenity's docs."""

    @classmethod
    def setUpClass(cls):
        """Sets up the Amenity class."""
        cls.base_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions."""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """Checks pycodestyle for amenity."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """Checks pycodestyle for test_amenity."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestAmenity(unittest.TestCase):
    """Tests class functionality."""

    def test_str(self):
        """Tests that __str__ is functioning normally."""
        self.assertEqual(self.__str__(), '[Amenity]')
