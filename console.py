#!/usr/bin/python3
"""
  The Console program.
  Contains the entry point of the command interpreter.
"""


import cmd
import sys
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


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
        if len(sys.argv) == 2:
            print("** class name missing **")
            return False
        elif sys.argv[2] in classes:
            new_inst = (sys.argv[2])()
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
        if len(sys.argv) == 2:
            print("** class name missing **")
            return False
        elif sys.argv[2] in classes:
            if len(sys.argv) > 3:
                key = sys.argv[2] + "." + sys.argv[3]
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
