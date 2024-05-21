#!/usr/bin/python3
"""This module contains the console class"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_brace = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_brace is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[: brackets.span()[0]])
            retll = [i.strip(",") for i in lexer]
            retll.append(brackets.group())
            return retll
    else:
        lexer = split(arg[: curly_brace.span()[0]])
        retll = [i.strip(",") for i in lexer]
        retll.append(curly_brace.group())
        return retll


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
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj.append(obj.__str__())
                elif len(args) == 0:
                    obj.append(obj.__str__())
            print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = parse(arg)
        objdict = storage.all()

        if len(args) < 2:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 3:
            print("** instance id missing **")
            return False
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) < 4:
            print("** attribute name missing **")
            return False
        if len(args) < 5:
            print("** value missing **")
            return False

        obj = objdict[instance_key]
        attribute_name = args[2]
        value = args[3]

        if attribute_name in obj.__class__.__dict__.keys():
            attribute_type = type(obj.__class__.__dict__[attribute_name])
            obj.__dict__[attribute_name] = attribute_type(value)
        else:
            obj.__dict__[attribute_name] = value

        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
