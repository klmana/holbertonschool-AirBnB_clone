#!/usr/bin/python3
"""
Unittest module for the FileStorage class.
"""

from models.engine import file_storage
from models import storage
from models.base_model import BaseModel
import json
import os
import pycodestyle
import unittest
import inspect
from datetime import datetime
FileStorage = file_storage.FileStorage


class TestDocsFileStorage(unittest.TestCase):
    """Tests for presence of FileStorage subclass documentation"""

    @classmethod
    def setUpClass(cls):
        """Easy access to all FileStorage functions"""
        cls.base_funcs = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for presence of module documentation"""
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for presence of FileStorage subclass documentation"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of documentation in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """Checks that file_storage complies with PEP 8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """Checks that test_file_storage complies with PEP 8 style"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files([
            'tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestFileStorage(unittest.TestCase):
    """Tests functionality of FileStorage subclass of BaseModel"""

    @classmethod
    def setUpClass(cls):
        """
        Creating an instance for use in tests
        (storage = FileStorage() in another init file)
        """
        cls.inst = storage

    def test_all(self):
        """Testing functionality of all"""
        test_dict = self.inst.all()
        self.assertEqual(self.inst._FileStorage__objects, test_dict)
        self.assertTrue(isinstance(test_dict, dict))

    def test_new(self):
        """Testing functionality of new"""
        for value in self.inst.all().values():
            test_value = value
        self.assertEqual(test_value, value)

    def test_save(self):
        """Testing functionality of save"""
        os.remove("file.json")
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(os.path.getsize("file.json"), 0)

    def test_reload(self):
        """Testing functionality of reload"""
        os.remove("file.json")
        self.inst.save()
        with open("file.json", "r") as f:
            before_reload = f.read()
        self.inst.reload()
        self.assertNotEqual(before_reload, self.inst._FileStorage__objects)
