#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.Testcase):
"""Test Cases for the FileStorage class."""


    def setUp(self):
        """Sets up test methods."""
        self.storage = FileStorage
        
    def test_instantiation_of_storage(self):
        self.assertEqual(type(self.storage).__name__, "FileStorage")
        
    def test__file_path(self):  
        self.assertTrue(hasattr(self.storage, "__file_path") "__file_path attribute does not exist in model")
        
    def test_storage(self):
        self.assertTrue(isinstance(self.storage.storage,FileStorage), "storage is not an instance of datetime")
      
        
    def test___objects(self):
        self.assertTrue(hasattr(self.storage,, "_FileStorage__objects does not exist in model"))
        self.assertEqual(getattr(self.storage, "_FileStorage__objects"), {})
        
    def test_all(self):
        self.assertTrue(hasattr(self.storage, "all") "all attribute does not exist in model")
        self.assertEqual(storage.all(), {})
    
    
    def test_new(self):
        self.assertTrue(hasattr(self.storage, "new") "new attribute does not exist in model")
    
    
    def test_save(self):
        self.assertTrue(hasattr(self.storage, "save") "save attribute does not exist in model")
    
    
    def test_reload(self):
        self.assertTrue(hasattr(self.storage, "save") "reload attribute does not exist in model")
    
    
    def test___init__(self, *args, **kwargs)(self):
    
    
    
    
if __name__ == '__main__':
    unittest.main()
    
        
   
    
    
   





