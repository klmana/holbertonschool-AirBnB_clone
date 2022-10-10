#!/usr/bin/python3
"""Contains tests for BaseModel class."""

import pycodestyle
import unittest
import datetime
import uuid
import inspect
from models import base_model
BaseModel = base_model.BaseModel


class TestDocsBaseModel(unittest.TestCase):
    """Tests for presence of BaseModel class documentation."""

    @classmethod
    def setUpClass(cls):
        """Easy access to all functions."""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for the presence of module documentation."""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of BaseModel class documentation."""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions."""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """Checks pycodestyle for base."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """Checks pycodestyle for test_base."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBaseModel(unittest.TestCase):
    """Tests class functionality."""

    def test_str(self):
        """Tests that __str__ is functioning normally."""
        self.assertEqual(self.__str__(), '[BaseModel]')
# INCOMPLETE
