#!/usr/bin/python3
""" Module for console that contains the entry point of command interpreter """


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

class_home = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "city": City,
    "Review": Review,
    "State": State
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ Exit the program when EOF (Ctrl+D) is entered """
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
        # OR
        # pass

    def do_create(self, line):
        """ Creates a new instance of class and save id """
        if line:
            try:
                glo_cls = globals().get(line, None)
                obj = glo_cls()
                obj.save()
                print(obj.id)  # Print id
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Prints the string representation of an instance """
        arrg = line.split()  # split and assign to variable

        if len(arrg) < 1:
            print("** class name missing **")
        elif arrg[0] not in class_home:
            print("** class doesn't exist **")
        elif len(arrg) < 2:
            print("** instances id missing **")
        else:
            new_string = f"{arrg[0]}.{arrg[1]}"
            if new_string not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[new_string])

    def do_destroy(self, line):
        """ Destroy an instance based on the class name and id """

        arrg = line.split()
        if len(arrg) < 1:
            print("** class name missing **")
        elif arrg[0] not in class_home:
            print("** class doesn't exist **")
        elif len(arrg) < 2:
            print("** instance id missing **")
        else:
            new_string = f"{arrg[0]}.{arrg[1]}"
            if new_string not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(new_string)
                storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instrrances """
        objects = []
        if line == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            strr = line.split(" ")
            if strr[0] not in class_home:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    clas = key.split(".")
                    if clas[0] == strr[0]:
                        objects.append(str(value))
                print(objects) 

    def do_update(self, line):
        """ Updates an instance based on the class name and id """
        arrg = line.split()
        if len(arrg) < 1:
            print("** class name missing **")
            return
        elif arrg[0] not in class_home:
            print("** class doesn't exist **")
            return
        elif len(arrg) < 2:
            print("** instance id missing **")
            return
        else:
            new_string = f"{arrg[0]}.{arrg[1]}"
            if new_string not in storage.all().keys():
                print("** no instance found **")
            elif len(arrg) < 3:
                print("** attribute name missing **")
                return
            elif len(arrg) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_string], arrg[2], arrg[3])
                storage.save()

    def do_count(self, line):
        """ Print and count all class instances """
        Cclass = globals().get(line, None)
        if Cclass is None:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == line:
                count += 1
            print(count)


    def default(self, line):
        
        if line in None:
            return

        cmdPattern = "^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        paramPattern = """^"([^"]+)"(?:,\s*(?:"([^"]+)"|(\{[^}]+\}))(?:,\s*(?:("?[^"]+"?)))?)?"""
        match = re.match(cmdPattern, line)
        if not match:
           super().default(line)
           return
        mName, method, param = match.groups()
        m = re.match(paramPattern, param)
        param = [item for item in match.groups() if item] if match else []

        cmd = " ".join([mName] + param)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
           return self.do_update(cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
