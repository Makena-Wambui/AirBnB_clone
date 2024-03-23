#!/usr/bin/python3

"""
This is the console module.
It is the entry point of the command interpreter.
It supplies one class: HBNBCommand

Import from cmd module, and use the Cmd class as a base class
for building command line interpreters.
"""

import cmd
import shlex
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class: HBNBCommand

    A sub class of class Cmd from the cmd module.

    All definitions for commands used in my console.

    Attrributes:
        prompt => (hbnb)
        classes = a list of classes accessible from the console.
    Methods:
        do_quit
        do_EOF
        empty_line
    """

    prompt = "(hbnb) "
    __classes = [
            "BaseModel", "User", "Place",
            "State", "City", "Amenity",
            "Review"
            ]

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
        line = shlex.split(line)
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
        line = shlex.split(line)

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
        line = shlex.split(line)

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
        line = shlex.split(line)

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
        line = shlex.split(line)

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

        # Retrieve the object based on class name and id
        o = my_dict[f"{line[0]}.{line[1]}"]

        if f"{line[0]}.{line[1]}" not in my_dict:
            print("** no instance found **")
            return False

        if len(line) == 2:
            print("** attribute name missing **")
            return False

        if len(line) == 3:
            attributes = line[2]

            try:
                pattern = re.search(r"\{(?:[^{}]|(?R))*\}", attributes)

                if pattern:
                    match_str = pattern.group(0)
                    dict_found = eval(match_str)

                    for key, val in dict_found.items():
                        if key in o.__dict__.keys():
                            o.__dict__[key] = val
                        else:
                            setattr(o, key, value)
                    storage.save()

            except Exception:
                print("** value missing **")
                return False

        if len(line) == 4:
            attribute_name = line[2]
            attribute_val = line[3]
            if attribute_name in o.__dict__.keys():
                val_type = type(attribute_val)
                setattr(o, attribute_name, val_type(attribute_val))
                storage.save()
            else:
                setattr(o, attribute_name, attribute_val)
                storage.save()

    def default(self, line):
        """
        By default, default is called if no command handler exists for
        the input entered.
        It prints an error message:ex => *** Unknown syntax: User.all()
        Then returns.
        This implementation overrides this behavior of the default method.
        """

        # first we specify a dictionary that contains all commands
        # and their respective handlers.
        # why are the values not strings?
        # Because they are references to methods and not literal strings.
        command_dict = {
                "create": self.do_create, "show": self.do_show,
                "update": self.do_update, "all": self.do_all,
                "destroy": self.do_destroy, "count": self.do_count
                }

        # lets call on split to split the input line,
        # with delimiter "." for ex User.all()
        # is split to a list of strings: ["User", "all()"]
        line_list = line.split(".")
        name = line_list[0]

        # now we focus on the command itself,
        # which is at index line_list[1]
        # we call split again to extract this command

        our_command_list = line_list[1].split("(")
        command = our_command_list[0]

        # the result looks like: ["all", ")"]

        # Lets add logic for handling commands like User.show(<id>)
        # and User.update("id", "name", "value")
        args_list = our_command_list[1].split(")")[0]

        # let us now separate id, attribute key, attribute value
        args = args_list.split(',')

        # lets check if it is a valid command in our
        # command_dict

        if command in command_dict.keys():
            # retrieve its value, the method
            value = command_dict[command]

            # Handle logic for update
            if command != "update":
                return value("{} {}".format(name, args_list))
            else:
                instance_id = args[0]
                k = args[1]
                v = args[2]
                # call update with necessary arguments
                return value("{} {} {} {}".format(name, instance_id, k, v))
        else:
            print(f"*** Unknown syntax: {line}")

        return False

    def do_count(self, line):
        """
        This method is called to retrieve the number of instances of a class.
        Should work like this:
            count User
            User.count()
        """

        # recall shlex tokenizes strings according to Unix Shell syntax
        # so this returns a list of strings.

        line = shlex.split(line)

        # initialize a counter to 0
        # keeps track of the number of instances.

        counter = 0

        # recall storage.all contains all objects;
        # key => Classname Id
        # value => the object itself
        for my_obj in storage.all().values():
            class_name = my_obj.__class__.__name__
            if line[0] == class_name:
                counter = counter + 1

        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
