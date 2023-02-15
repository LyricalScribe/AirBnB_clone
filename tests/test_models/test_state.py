#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.Testcase):
"""Test Cases for the Amenity class."""


    def setUp(self):
    """Sets up test methods."""
        self.state = State()
        self.state_2 = State()
        
    def test_state_id(self):
        self.assertTrue(hasattr(self.state, "state_id"),"state_id attribute does not exist in model")
        self.assertNotEqual(self.state.id, self.state_2.id)
    
    def test_name(self):
        self.assertTrue(hasattr(self.state, "name"),"name attribute does not exist in model")
        self.name = "Mpumalanga"
        self.assertEqual(self.name, "Mpumalanga")
    
    def test_id(self):
        self.assertNotEqual(self.state.id, self.place_2.id)
        self.assertTrue(hasattr(self.state, "id"))
     
    def test_created_at(self):
        self.assertTrue(hasattr(self.state, "created_at"),"created_at attribute does not exist in model")
        self.assertTrue(isinstance(self.state.created_at,datetime), "Place is not an instance of datetime")
        
    def test_updated_at(self):
        self.assertTrue(hasattr(self.state, "updated_at"), "updated_at attribute does not exist in model")
        self.assertTrue(isinstance(self.state.updated_at,datetime), "updated_at is not an instance of datetime")
    
if __name__ == "__main__":
    unittest.main()    