#!/usr/bin/python3
import unittest
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.Testcase):
"""Test Cases for the Amenity class."""

    def setUp(self):
    """Sets up test methods."""
        self.user = User()  

    def test_email(self):
        self.assertTrue(hasattr(self.user.email, "email"),"email attribute does not exist in model")

    def test_password(self):
        self.assertTrue(hasattr(self.user.password, "city_id"),"password attribute does not exist in model")
    
   
    def test_first_name(self):
        self.assertTrue(hasattr(self.user.first_name, "first_name"),"first_name attribute does not exist in model")
        self.first_name = "Denny"
        self.assertEqual(self.first_name, "Denny")
    
    
    def test_last_name(self):
        self.assertTrue(hasattr(self.user.last_name, "last_name"),"last_name attribute does not exist in model")
        self.last_name = "Msika"
        self.assertEqual(self.last_name, "Msika")
        
    def test_id(self):
        self.assertNotEqual(self.user.id, self.place_2.id)
        self.assertTrue(hasattr(self.user, "id"))
     
    def test_created_at(self):
        self.assertTrue(hasattr(self.user, "created_at"),"created_at attribute does not exist in model")
        self.assertTrue(isinstance(self.user.created_at,datetime), "Place is not an instance of datetime")
        
    def test_updated_at(self):
        self.assertTrue(hasattr(self.user, "updated_at"), "updated_at attribute does not exist in model")
        self.assertTrue(isinstance(self.user.updated_at,datetime), "updated_at is not an instance of datetime")
        
if __name__ == "__main__":
    unittest.main()