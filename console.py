#!/usr/bin/python3
""" Module for consule that contains the entry point of command interpreter """

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_quit(self, line):
        """ Quit command to exit program """
        print("Good Bye")
        return True

    def do_EOF(self, line):
        """ Exit the program when EOF (Ctrl+D) is entered """
        print() #  Print a newline before exiting
        return True

    def help_quit(self):
        """ When two arguments involve """
        print('\n'.join(["Quit command to exit program"]))

    def emptyline(self):
        """ Overwrite the empty line """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()