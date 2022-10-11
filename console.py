#!/usr/bin/python3
"""
  The Console program.


  Contains the entry point of the command interpreter.
"""


import cmd
import sys


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
