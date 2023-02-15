#!/usr/bin/python3
import unittest
from models.city import City



class TestCity(unittest.Testcase):
"""Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        self.city = City()
        self.city_2 = City()
        
    def test_state_id(self):
        self.assertTrue(hasattr(self.city, "state_id"),"state_id attribute does not exist in model")
        self.assertNotEqual(self.city.id, self.city_2.id)
    
    def test_name(self):
        self.assertTrue(hasattr(self.city, "name"),"name attribute does not exist in model")
        self.name = "Nelspruit"
        self.assertEqual(self.name, "Nelspruit")
    
    def test_id(self):
        self.assertNotEqual(self.city.id, self.place_2.id)
        self.assertTrue(hasattr(self.city, "id"))
     
    def test_created_at(self):
        self.assertTrue(hasattr(self.city, "created_at"),"created_at attribute does not exist in model")
        self.assertTrue(isinstance(self.city.created_at,datetime), "Place is not an instance of datetime")
        
    def test_updated_at(self):
        self.assertTrue(hasattr(self.city, "updated_at"), "updated_at attribute does not exist in model")
        self.assertTrue(isinstance(self.city.updated_at,datetime), "updated_at is not an instance of datetime")
       
if __name__ == "__main__":
    unittest.main()
