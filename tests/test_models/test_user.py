#!/usr/bin/python3
"""Contains tests for User class."""

import pycodestyle
import unittest
import datetime
import uuid
import inspect
import models

from models.base_model import BaseModel
from models.user import User


class TestDocsUser(unittest.TestCase):
    """Tests for the User's docs."""

    @classmethod
    def setUpClass(cls):
        """Sets up the User class."""
        cls.base_funcs = inspect.getmembers(User, inspect.isfunction)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions."""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """Checks pycodestyle for user."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """Checks pycodestyle for test_user."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestUser(unittest.TestCase):
    """Tests class functionality."""
