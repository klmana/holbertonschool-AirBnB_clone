#!/usr/bin/python3
"""
The Console program.
Contains the entry point of the command interpreter.
"""


import cmd
import sys
import models
import shlex
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

classes = {"BaseModel": BaseModel, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review, "User": User}


class HBNBCommand(cmd.Cmd):
    """Contains command prompts for HBNB program's intepreter."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command - exits the program."""
        return True

    def do_EOF(self, arg):
        """EOF command - Crtl-D to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Empty line - does nothing."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] in classes:
            new_inst = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(new_inst.id)
        new_inst.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
                    return False
            else:
                print("** instance id missing **")
                return False
        else:
            print("** class doesn't exist **")
            return False

    def do_destroy(self, arg):
        """
        Deletes an instance based upon
        class name and id, with changes saved
        to JSON file.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    del (models.storage.all()[key])
                    models.storage.save()
                else:
                    print("** no instance found **")
                    return False
            else:
                print("** instance id missing **")
                return False
        else:
            print("** class doesn't exist **")
            return False

    def do_all(self, arg):
        """
        Prints all string representations of instances
        """
        o_list = []
        args = shlex.split(arg)
        if len(args) == 0:
            for key in models.storage.all():
                o_list.append(str(models.storage.all()[key]))
                print(o_list)
        if len(args) == 1:
            if args[0] in classes:
                for key in models.storage.all():
                    o_list.append(str(models.storage.all()[key]))
                    print(o_list)
            else:
                print("** class doesn't exist **")
                return False

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[key],
                                    args[2], args[3])
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
