#!/usr/bin/python3
"""This module contains the console class"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This class contains the console class
    Attributes:
        prompt (str): The prompt to display
        __classes (dict): Dictionary of classes
    """

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in storage.all().values():
            if not arg or obj.__class__.__name__ == arg:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        try:
            value = eval(args[3])
        except (SyntaxError, NameError):
            value = args[3]
        setattr(obj, args[2], value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
