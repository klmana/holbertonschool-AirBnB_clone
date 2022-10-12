#!/usr/bin/python3
"""Contains tests for Review class."""

import pycodestyle
import unittest
import datetime
import uuid
import inspect

from models.base_model import BaseModel
from models.review import Review


class TestDocsReview(unittest.TestCase):
    """Tests for the Review's docs."""

    @classmethod
    def setUpClass(cls):
        """Sets up the Review class."""
        cls.base_funcs = inspect.getmembers(Review, inspect.isfunction)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions."""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """Checks pycodestyle for review."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """Checks pycodestyle for test_review."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestReview(unittest.TestCase):
    """Tests class functionality."""

    def test_str(self):
        """Tests that __str__ is functioning normally."""
        self.assertEqual(self.__str__(), '[Review]')
