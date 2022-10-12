#!/usr/bin/python3
"""
  The Console program.
  Contains the entry point of the command interpreter.
"""


import cmd
import sys
import models
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
        args = arg.split()
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
        args = arg.split()
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
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    del(models.storage.all()[key])
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
        args = arg.split()
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
        """
        Updates an instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False
        key = args[0] + "." + args[1]
        if key in models.storage.all():
            setattr(models.storage.new()[key], arg[2], arg[3])
            models.storage.save()
        else:
            print("** no instance found **")
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
