#!/usr/bin/python3
from models.base_model import BaseModel

"""USer module for this project"""


class User(BaseModel):
    """User Class module"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
