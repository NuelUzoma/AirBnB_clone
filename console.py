#!/usr/bin/python3
"""
The console command line intepreter
"""

import json
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage, User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """The End of File for the console"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to JSON File"""
        if line == "":
            print("** class name missing **")
            return

        try:
            obj = eval(line)()
        except NameError:
            print("** class doesn't exists **")
            return

        print(obj.id)
        obj.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""
        line_split = line.split()
        if line == "":
            print("** class name missing **")
        elif line_split[0] != "BaseModel":  # show MyModel
            print("** class doesn't exist **")
        elif len(line_split) != 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line_split[0], line_split[1])
            objs = storage.all()
            if key in objs.keys():
                print(objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on class name and id"""
        line_splits = line.split()
        if line == "":
            print("** class name missing **")
        elif line_splits[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(line_splits) != 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line_splits[0], line_splits[1])
            objs = storage.all()
            if key in objs.keys():
                del (objs[key])
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        line_splt = line.split()
        objectts = storage.all()
        if len(line_splt) > 0 and line_splt[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            list_objs = []
            if len(line_splt) == 0:
                for value in objectts.values():
                    list_objs.append(str(value))
            else:
                for value in objectts.values():
                    if isinstance(value, eval(line_splt[0])):
                        list_objs.append(str(value))
            print(list_objs)

    def do_update(self, line):
        """Updates an instance based on class name and id"""
        line_splts = line.split()
        if line == "":  # update
            print("** class name missing **")
        elif line_splts[0] != "BaseModel":  # update MymOdel
            print("** class doesn't exist **")
        elif len(line_splts) == 1:  # update BaseModel <no id>
            print("** instance id missing **")
        elif len(line_splts) == 2:  # update BaseModel 241545
            print("** attribute name missing **")
        elif len(line_splts) == 3:
            print("** value missing **")
        else:
            key_1 = "{}.{}".format(line_splts[0], line_splts[1])
            dict_1 = storage.all()
            if key_1 in dict_1.keys():
                obj_1 = dict_1[key_1]
                obj_replace = line_splts[3].replace('"', '')
                obj_1.__dict__[line_splts[2]] = obj_replace
                dict_1[key_1] = obj_1
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
