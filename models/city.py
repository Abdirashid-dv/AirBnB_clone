#!/usr/bin/python3
"""Module for City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel

    Attributes:
        state_id (str): the state id
        name (str): name of the city
    """

    state_id = ""
    name = ""
