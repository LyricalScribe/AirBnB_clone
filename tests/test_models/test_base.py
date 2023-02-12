#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

"""Unittest for BaseModel()
"""


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.now())
        self.assertIsInstance(model.updated_at, datetime.now())

    def test_str(self):
        model = BaseModel()
        self.assertEqual(
            str(model),
            "[BaseModel] ({}) {}".format(model.id, model.__dict__)
            )

    def test_save(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        my_dict = model.to_dict()
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertEqual(my_dict["id"], model.id)
        self.assertEqual(my_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], model.updated_at.isoformat())
