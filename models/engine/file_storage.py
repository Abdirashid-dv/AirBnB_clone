#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
        deserializes JSON file to instances
    Attributes:
        __file_path (str): the path to the JSON file
        __objects (dict): a dictionary of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        Returns:
            dict: __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (BaseModel): object to be set
        """
        obj_name = obj.__class__.__name__
        key = "{}.{}".format(obj_name, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
