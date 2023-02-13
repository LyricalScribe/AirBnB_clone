#!/usr/bin/python3
import unittest
from base_model import BaseModel
from datetime import datetime
"""Unittest for BaseModel()"""

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set Up instances"""
        self.model = BaseModel()
        self.model_2 = BaseModel()

    
    def test_id(self):
      
        self.assertNotEqual(self.model.id, self.model_2.id)
        self.assertTrue(hasattr(self.model, "id"))
        
    def test_created_at(self):
        self.assertTrue(hasattr(self.model, "created_at"),"created_at attribute does not exist in model")
        self.assertTrue(isinstance(self.model.created_at,datetime), "created at is not an instance of datetime")
        
        
    def test_updated_at(self):
        self.assertTrue(hasattr(self.model, "updated_at"), "updated_at attribute does not exist in model")
        self.assertTrue(isinstance(self.model.updated_at,datetime), "updated_at is not an instance of datetime")
        
    def test_instantiation_of_model(self):
        self.assertEqual(type(self.model).__name__, "BaseModel")
        
    def test_dict(self):
    
        _dict = self.model.to_dict()
        self.assertIsInstance(_dict, dict)
        self.assertEqual(_dict["__class__"], "BaseModel")
        self.assertEqual(_dict["id"], self.model.id)
        self.assertEqual(_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(_dict["updated_at"], self.model.updated_at.isoformat())
        
    def test_str(self):
        self.assertEqual(str(self.model),"[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__))
        
