#!/usr/bin/python3

"""
This is the console module.
It is the entry point of the command interpreter.
It supplies one class: HBNBCommand

Import from cmd module, and use the Cmd class as a base class
for building command line interpreters.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class: HBNBCommand

    A sub class of class Cmd from the cmd module.

    Attrributes:
        prompt => (hbnb)
    Methods:
        do_quit
        do_EOF
        empty_line
    """

    prompt = "(hbnb)"

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
