#!/usr/bin/python3

from models.base_model import BaseModel


"""The state module"""


class Review(BaseModel):
    """Review Class module"""
    place_id = ""
    user_id = ""
    text = ""
