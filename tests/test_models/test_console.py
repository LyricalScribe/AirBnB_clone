#!/usr/bin/ dnv python3

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
import sys
from io import StringIO
import re
import os


class TestConsole(unittest.Testcase):
"""Test Cases for the Console"""

    def setUp(self):
        """Sets up test case"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

