#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.Testcase):
"""Test Cases for the Amenity class."""
    
    def setUp(self):
    """Sets up test methods."""
        self.place = Place()
        self.place_2 = Place()
        
    def test_id:
        self.assertNotEqual(self.place.id, self.place_2.id)
        
    def test_city_id(self):
        self.assertTrue(hasattr(self.place, "city_id"),"city_id attribute does not exist in Place model")
        city_id = "39c614f2-a472-4714-850b-3cc39f57e8b9"
        self.place.city_id = city_id
        self.assertEqual(self.place.city_id,city_id)

    def test_user_id(self):
        self.assertTrue(hasattr(self.place, "user_id"),"user_id attribute does not exist in Place model")

    def test_name(self):
        self.assertTrue(hasattr(self.place, "name"),"name attribute does not exist in Place model")
        
    def test_id(self):
        self.assertNotEqual(self.place.id, self.place_2.id)
        self.assertTrue(hasattr(self.place, "id"))
     
    def test_created_at(self):
        self.assertTrue(hasattr(self.place, "created_at"),"created_at attribute does not exist in model")
        self.assertTrue(isinstance(self.place.created_at,datetime), "Place is not an instance of datetime")
        
    def test_updated_at(self):
        self.assertTrue(hasattr(self.place, "updated_at"), "updated_at attribute does not exist in model")
        self.assertTrue(isinstance(self.place.updated_at,datetime), "updated_at is not an instance of datetime")
      
        
