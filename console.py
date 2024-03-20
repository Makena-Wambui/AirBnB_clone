#!/usr/bin/python3

"""
This is the console module.
It is the entry point of the command interpreter.
It supplies one class: HBNBCommand

Import from cmd module, and use the Cmd class as a base class
for building command line interpreters.
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class: HBNBCommand

    A sub class of class Cmd from the cmd module.

    Attrributes:
        prompt => (hbnb)
        classes = a list of classes accessible from the console.
    Methods:
        do_quit
        do_EOF
        empty_line
    """

    prompt = "(hbnb)"
    __classes = ["BaseModel"]

    def emptyline(self):
        """
        By default, empty_line reruns the last nonempty entry.

        Override it here by making it execute nothing.
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        End Of File Marker is sent to this method.

        Provides a way of cleanly exiting the program.
        """
        print()
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        # lets parse the line with split()
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            name = eval(line[0])
            print(name().id)
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        as a list.
        Should work like this: all <class_name> or all
        """
        # parse the command line
        line = line.split()

        if len(line) > 0 and line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        else:
            # initialize an empty list to store the string representations.
            my_list = []

            # call all method that returns a dictionary containing all objects.
            my_dict = storage.all()

            # only interested in the values of this dict
            for o in my_dict.values():
                name = o.__class__.__name__
                if len(line) > 0 and line[0] == name:
                    o = str(o)
                    my_list.append(o)

                if len(line) == 0:
                    o = str(o)
                    my_list.append(o)
            print(my_list)

    def do_show(self, line):
        """
        Command handler for the show command.
        Prints the string representation of an instance based
        on the class name and id.
        """
        # parse line
        line = line.split()

        # my_dict is a dict containing all objects.
        # all returns this dictionary
        my_dict = storage.all()

        if len(line) == 0:
            print("** class name missing **")

        elif line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(line) == 1:
            print("** instance id missing **")

        elif f"{line[0]}.{line[1]}" not in my_dict:
            print("** no instance found **")

        else:
            print(my_dict[f"{line[0]}.{line[1]}"])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Then changes are saved into the JSON file
        """
        # start with line parsing
        line = line.split()

        if len(line) == 0:
            print("** class name missing **")
            return False

        if line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        if len(line) == 1:
            print("** instance id missing **")
            return False

        # reference to the dict that stores all objects.
        my_dict = storage.all()
        if f"{line[0]}.{line[1]}" not in my_dict:
            print("** no instance found **")
        else:
            del my_dict[f"{line[0]}.{line[1]}"]
            storage.save()

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        Changes then saved into the JSON file.
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        line = line.split()

        if len(line) == 0:
            print("** class name missing **")
            return False

        if line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        if len(line) == 1:
            print("** instance id missing **")
            return False

        my_dict = storage.all()
        if f"{line[0]}.{line[1]}" not in my_dict:
            print("** no instance found **")
            return False

        if len(line) == 2:
            print("** attribute name missing **")
            return False

        if len(line) == 3:
            print("** value missing **")
            return False

        # Retrieve the object based on class name and id
        o = my_dict[f"{line[0]}.{line[1]}"]

        # check if that attribute name already exists
        if line[2] in o.__dict__.keys():
            # get value of this attribute and its type
            value = o.__dict__[line[2]]
            my_type = type(value)

            # typecast and set
            setattr(o, line[2], my_type(line[3]))
            storage.save()
        else:
            setattr(o, line[2], line[3])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
