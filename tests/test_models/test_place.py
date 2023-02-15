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
     
    def test_description(self):
        self.assertTrue(hasattr(self.place.description, "description"),"description does not exist in Place model")
        
    def test_number_rooms(self):
        self.assertTrue(hasattr(self.place.number_rooms, "number_rooms"),"number_rooms does not exist in Place model")
        self.place.number_rooms = "3"
        self.assertEqual(self.place.number_rooms, "3")
        
    def test_number_bathrooms(self):
        self.assertTrue(hasattr(self.place.number_bathrooms, "number_bathrooms"),"number_rooms does not exist in Place model")
        self.place.number_bathrooms = "2"
        self.assertEqual(self.place.number_bathrooms, "2")
        
    def test_max_guest(self):
        self.assertTrue(hasattr(self.place.max_guest, "max_guest"),"max_guest does not exist in Place model")
        self.place.max_guest = "8"
        self.assertEqual(self.place.max_guest, "8")
    
    def test_price_by_night(self):
        self.assertTrue(hasattr(self.place.price_by_night, "price_by_night"),"price_by_night does not exist in Place model")
        self.place.price_by_night = "$200"
        self.assertEqual(self.place.price_by_night, "$200")
    
    def test_latitude(self):
        self.assertTrue(hasattr(self.place.latitude, "latitude"),"latitude does not exist in Place model")
        
    def test_longitude(self):
        self.assertTrue(hasattr(self.place.longitude, "longitude"),"longitude does not exist in Place model")
        
    def test_amenity_ids(self):
        self.assertTrue(hasattr(self.place.amenity_ids, "amenity_ids"),"amenity_ids does not exist in Place model")
        
    def test_created_at(self):
        self.assertTrue(hasattr(self.place, "created_at"),"created_at attribute does not exist in Place model")
        self.assertTrue(isinstance(self.place.created_at,datetime), "Place is not an instance of datetime")
        
    def test_updated_at(self):
        self.assertTrue(hasattr(self.place, "updated_at"), "updated_at attribute does not exist in Place model")
        self.assertTrue(isinstance(self.place.updated_at,datetime), "updated_at is not an instance of datetime")
        
if __name__ == "__main__":
    unittest.main()
      
        
