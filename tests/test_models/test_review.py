#!/usr/bin/python3
import unittest
from models.review import Review




class TestReview(unittest.Testcase):
"""Test Cases for the Review class."""


    def setUp(self):
    """Sets up test methods."""
        self.review = Review()
        
    def test_text(self):
    review_text = "good place"
    self.review.text = review_text
    assertEqual(self.review.text, review_text)
    self.assertTrue(hasattr(self.review, "Review"),"review attribute does not exist in model")
    
    def test_id(self):
        self.assertNotEqual(self.review.id, self.place_2.id)
        self.assertTrue(hasattr(self.review, "id"))
     
    def test_created_at(self):
        self.assertTrue(hasattr(self.review, "created_at"),"created_at attribute does not exist in model")
        self.assertTrue(isinstance(self.review.created_at,datetime), "Place is not an instance of datetime")
        
    def test_updated_at(self):
        self.assertTrue(hasattr(self.review, "updated_at"), "updated_at attribute does not exist in model")
        self.assertTrue(isinstance(self.review.updated_at,datetime), "updated_at is not an instance of datetime")
