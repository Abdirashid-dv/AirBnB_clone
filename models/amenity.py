#!/usr/bin/python3
"""Module for Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel

    Attributes:
        name (str): name of the amenity
    """

    name = ""
