#!/usr/bin/python3
"""__init__.py file for the models module"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
