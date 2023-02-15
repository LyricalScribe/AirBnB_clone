#!/usr/bin/python3
import unittest

from models.amenity import Amenity



class TestAmenity(unittest.Testcase):
"""Test Cases for the Amenity class."""

    def setUp(self):
    """Sets up test methods."""
        self.amenity = Amenity()
        self.amenity_2 = Amenity()
        
    def test_instantiation_of_model(self):
        self.assertEqual(type(self.model).__name__, "Amenity")
    
    def test_name(self):
        self.assertTrue(hasattr(self.amenity, "name"),"name attribute does not exist in model")
        self.amenity.name = "Bathroom"
        self.assertEqual(self.amenity.name, "Bathroom")
        
    def test_id(self):
        self.assertNotEqual(self.amenity.id, self.amenity_2.id)
        self.assertTrue(hasattr(self.amenity, "id"))
     
    def test_created_at(self):
        self.assertTrue(hasattr(self.amenity, "created_at"),"created_at attribute does not exist in model")
        self.assertTrue(isinstance(self.amenity.created_at,datetime), "Amenity is not an instance of datetime")
        
    def test_updated_at(self):
        self.assertTrue(hasattr(self.amenity, "updated_at"), "updated_at attribute does not exist in model")
        self.assertTrue(isinstance(self.amenity.updated_at,datetime), "updated_at is not an instance of datetime")
        
        
if __name__ == "__main__":
    unittest.main()
    
   