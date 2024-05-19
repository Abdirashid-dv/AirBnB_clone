#!/usr/bin/python3
"""This module contains the FileStorage class"""
import json


class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON file to instances
    Attributes:
        __file_path (str): the path to the JSON file
        __objects (dict): a dictionary of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns the dictionary __objects
        Returns:
            dict: __objects
        """
        return self.__objects

    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (BaseModel): object to be set
        """
        obj_name = obj.__class__.__name__
        key = "{}.{}".format(obj_name, obj.id)
        self.__objects[key] = obj

    def save(self) -> None:
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self) -> None:
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, obj in obj_dict.items():
                    self.__objects[key] = eval(obj["__class__"])(**obj)
        except FileNotFoundError:
            return
