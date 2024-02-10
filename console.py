#!/usr/bin/python3
"""Module for console that contains the entry point of command interpreter"""

import cmd
import re
import models
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Entry point defines a prompt (hbnb)"""
    __locals = locals()
    prompt = '(hbnb) '
    __models = ["BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]

    def get_method_and_params(self, arg):
        method_name = ""
        parameters - []
        in_bracket = False

        for i in range(len(arg)):
            if not in_bracket and arg[i] not in "()":
                method_name += arg[i]
            elif not in_bracket and arg[i] in "(":
                in_bracket = not in_bracket
            else:
                parameters = arg[i:-1].split(", ")
                break

        return method_name, parameters

    def default(self, arg):
        if '.' in arg:
            class_name, raw_method_name = arg.split(".", 1)
            method_name, params = self.get_method_and_params(
                raw_method_name)

            string_params = " ".join([class_name, " ".join(params)])
            self.__locals["do_" + method_name](self, string_params)
        else:
            Cmd.default(self, arg)

    def do_EOF(self, line):
        """Exit the program when EOF (Ctrl+D) is entered"""
        print("")  # Print a newline before exiting
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print("Good Bye!")
        return True

    def help_quit(self):
        """when two arguments involve"""
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_create(self, arg):
        """This creates a command a new instance"""
        if not arg:
            print('** class name missing **')
            return

        class_name = arg.strip()
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints string repr of an instance based on the class name"""
        try:
            [class_name, instance_id] = self.get_args(arg)

            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            print(retrieved_record)
        except Exception:
            pass

    def do_destroy(self, arg):
        """Destroys an instance of a class based on the classs name and id"""
        try:
            [class_name, instance_id] = self.get_args(arg)

            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            storage.destroy(retrieved_record)
        except Exception:
            pass

    def do_all(self, arg):
        """Prints string repr of all instances based on or not class name"""
        if not arg:
            instances = storage.all()
            instance_list = []
            for instance in instances.values():
                instance_list.append(str(instance))
            print(instance_list)
        else:
            class_name = arg.strip()
            if class_name not in self.__models:
                print("** class doesn't exist **")
                return

            file_storage = storage._FileStorage__objects
            instance_list = []
            for instance in file_storage.values():
                if instance['__class__'] == class_name:
                    instance_list.append(str(instance))
            print(instance_list)

    def do_update(self, arg):
        """This updates an instance based on the class name and id"""
        args = self.get_update_args(arg)

        if args is None:
            return

        [class_name, instance_id, attribute, value] = args

        try:
            record = self.find_record(class_name, instance_id)
            retrieved_record = globals()[class_name](**record)
            setattr(retrieved_record, attribute, value)
            setattr(retrieved_record, "updated_at", datetime.now())
            storage.new(retrieved_reord)
        except Exception:
            pass

    def get_update_args(self, arg):
        args = arg.split()

        if args:
            if len(args) > 1:
                if len(args) > 2:
                    if len(args) > 3:
                        return [*args[:3] + [self.get_value(args)]]
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** instance id missing **")
        else:
            print('** class name missing **')

    def get_value(self, args):
        found = False
        arr = " ".join([str(item) for item in args[3:]])
        value = ""

        for k in arr:
            if found and k == '"':
                found = not found
                break
            elif not found and k == '"':
                found = not found
            else:
                value += k

        return value

    def get_args(self, arg):
        args = arg.split()

        if args:
            if len(args) == 2:
                return args
            else:
                print("** instance id missing **")
        else:
            print('** class name missing **')
        return None

    def find_record(self, class_name, instance_id):

        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        all = storage.all()

        try:
            record = all[class_name + "." + instance_id]
            return record
        except Exception:
            print("** no instance found **")
            return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
