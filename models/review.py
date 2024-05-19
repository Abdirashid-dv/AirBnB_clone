#!/usr/bin/python3
"""Module for Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel

    Attributes:
        place_id (str): the place id
        user_id (str): the user id
        text (str): the review text
    """

    place_id = ""
    user_id = ""
    text = ""
