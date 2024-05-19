#!/usr/bin/python3
"""Module for State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel

    Attributes:
        name (str): name of the state
    """

    name = ""
