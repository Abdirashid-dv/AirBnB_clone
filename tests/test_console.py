#!/usr/bin/python3
"""This module contains the console class

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand_prompting(unittest.TestCase):
    def test_prompt(self):
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")


class TestHBNBCommand_help(unittest.TestCase):
    def test_help_quit(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIn("Quit command to exit the program", f.getvalue())

    def test_help_EOF(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertIn("Exit the program", f.getvalue())


class TestHBNBCommand_exit(unittest.TestCase):
    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    def setUp(self):
        storage.all().clear()

    def test_create_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertIn("** class name missing **", f.getvalue())

    def test_create_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_create_valid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)
            self.assertIn("BaseModel.{}".format(f.getvalue().strip()), storage.all())


class TestHBNBCommand_show(unittest.TestCase):
    def setUp(self):
        storage.all().clear()
        self.obj = BaseModel()
        self.obj.save()

    def test_show_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertIn("** class name missing **", f.getvalue())

    def test_show_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_show_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_show_invalid_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234")
            self.assertIn("** no instance found **", f.getvalue())

    def test_show_valid(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {self.obj.id}")
            self.assertIn(str(self.obj), f.getvalue())


class TestHBNBCommand_all(unittest.TestCase):
    def setUp(self):
        storage.all().clear()
        self.obj = BaseModel()
        self.obj.save()

    def test_all_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_all_no_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertIn(str(self.obj), f.getvalue())

    def test_all_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn(str(self.obj), f.getvalue())


class TestHBNBCommand_destroy(unittest.TestCase):
    def setUp(self):
        storage.all().clear()
        self.obj = BaseModel()
        self.obj.save()

    def test_destroy_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertIn("** class name missing **", f.getvalue())

    def test_destroy_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_destroy_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_destroy_invalid_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234")
            self.assertIn("** no instance found **", f.getvalue())

    def test_destroy_valid(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {self.obj.id}")
            self.assertNotIn(f"BaseModel.{self.obj.id}", storage.all())


class TestHBNBCommand_update(unittest.TestCase):
    def setUp(self):
        storage.all().clear()
        self.obj = BaseModel()
        self.obj.save()

    def test_update_missing_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertIn("** class name missing **", f.getvalue())

    def test_update_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            self.assertIn("** class doesn't exist **", f.getvalue())

    def test_update_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertIn("** instance id missing **", f.getvalue())

    def test_update_invalid_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234")
            self.assertIn("** no instance found **", f.getvalue())

    def test_update_missing_attr_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {self.obj.id}")
            self.assertIn("** attribute name missing **", f.getvalue())

    def test_update_missing_value(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {self.obj.id} name")
            self.assertIn("** value missing **", f.getvalue())

    def test_update_valid(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {self.obj.id} name test")
            self.assertEqual(self.obj.name, "test")
            self.assertIn("test", f.getvalue())


if __name__ == "__main__":
    unittest.main()
