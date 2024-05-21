#!/usr/bin/python3
"""Defines unittests for base.py"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

class TestBase(unittest.TestCase):
    """Define unittests for class Base"""

    def test_no_arg(self):
        a1 = Base()
        a2 = Base()
        self.assertEqual(a1.id, a2.id - 1)

    def test_None_id(self):
        a1 = Base(None)
        a2 = Base(None)
        self.assertEqual(a1.id, a2.id - 1)

    def test_unique_id(self):
        self.assertEqual(10, Base(10).id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_create_doc(self):
        """Test create doc"""
        self.assertIsNotNone(Base.create.__doc__)

    def test_save_to_file_doc(self):
        """Test save to file"""
        self.assertIsNotNone(Base.save_to_file.__doc__)

    def test_from_json_string_doc(self):
        """Test from json"""
        self.assertIsNotNone(Base.from_json_string.__doc__)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

class TestBase_from_json_string(unittest.TestCase):
   """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Deany created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()
