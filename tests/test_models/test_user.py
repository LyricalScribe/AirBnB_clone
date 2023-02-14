#!/usr/bin/python3
import unittest



class TestUser(unittest.TestCase):

    def setUp(self):
        """Set Up instances"""
        self.user = User()
        self.user_2 = User()

  