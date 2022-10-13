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

    @classmethod
    def setUpClass(cls):
        """
        Initialisation for subsequent tests -
        creating an instance of BaseModel class and two attributes
        """
        cls.inst = BaseModel()
        cls.inst.height = 179
        cls.inst.street = 'Gloucester'

    def test_init(self):
        """Testing that __init__ functions correctly"""
        self.assertEqual(self.inst.height, 179)
        self.assertTrue(isinstance(self.inst, BaseModel))

    def test_str(self):
        """Testing that __str__ functions correctly"""
        test_string = f"[BaseModel] ({self.inst.id}) {self.inst.__dict__}"
        self.assertEqual(str(self.inst), test_string)

    def test_save(self):
        """Testing the save functions correctly"""
        old_updated = self.inst.updated_at
        old_created = self.inst.created_at
        self.inst.save()
        new_updated = self.inst.updated_at
        new_created = self.inst.created_at
        self.assertEqual(old_created, new_created)
        self.assertNotEqual(old_updated, new_updated)

    def test_to_dict(self):
        """Testing that to_dict functions correctly"""
        test_dict = self.inst.to_dict()
        self.assertTrue(isinstance(test_dict, dict))
        self.assertEqual(test_dict["id"], self.inst.id)
        self.assertEqual(test_dict["updated_at"],
                         self.inst.updated_at.isoformat())
