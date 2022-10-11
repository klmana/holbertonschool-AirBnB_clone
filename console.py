#!/usr/bin/python3
"""
  The Console program.


  Contains the entry point of the command interpreter.
"""


import cmd
import sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Contains command prompts for HBNB program's intepreter."""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command - exits the program."""
        return True

    def do_EOF(self, arg):
        """EOF command - Crtl-D to exit the program."""
        print()
        return True

    def emptyline(self):
        """Empty line - does nothing."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel."""
        if len(arg) == "":
            print("** class name missing **")
            return False
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, arg):
        """Prints the string representation of an instance
        \based on the class name and id."""
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
