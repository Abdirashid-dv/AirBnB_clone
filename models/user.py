#!/usr/bin/python3
"""Module for User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel

    Attributes:
        email (str): the user's email
        password (str): the user's password
        first_name (str): the user's first name
        last_name (str): the user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
