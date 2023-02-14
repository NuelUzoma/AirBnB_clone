#!/usr/bin/python3
"""
The console command line intepreter
"""

import json
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.engine.file_storage import *
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    """Simple command processor example"""
    prompt = '(hbnb) '

    def default(self, line: str) -> None:
        """This function gets called when the command doesnt
        have an implemetation

        Args:
            line (str): This is the command that is passed to the prompt
        """
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in ["BaseModel",
                               "Amenity",
                               "City",
                               "Place",
                               "Review",
                               "State",
                               "User"]:
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                for attribute, value in d.items():
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """The End of File for the console"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of a class and saves it to JSON File"""
        if line == "":
            print("** class name missing **")
            return

        try:
            obj = eval(line)()
        except NameError:
            print("** class doesn't exist **")
            return

        print(obj.id)
        obj.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""
        line_split = line.split()
        if line == "":
            print("** class name missing **")
        elif line_split[0] not in ["BaseModel",
                                   "Amenity",
                                   "City",
                                   "Place",
                                   "Review",
                                   "State",
                                   "User"
                                   ]:  # show MyModel
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
        elif line_splits[0] not in ["BaseModel",
                                    "Amenity",
                                    "City",
                                    "Place",
                                    "Review",
                                    "State",
                                    "User"]:
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
        if len(line_splt) > 0 and line_splt[0] not in ["BaseModel",
                                                       "Amenity",
                                                       "City",
                                                       "Place",
                                                       "Review",
                                                       "State",
                                                       "User"]:
            print("** class doesn't exist **")
        else:
            list_objs = []
            if len(line_splt) == 0:
                for value in objectts.values():
                    list_objs.append(str(value))
            else:
                for value in objectts.values():
                    if type(value) == eval(line_splt[0]):
                        list_objs.append(str(value))
            print(list_objs)

    def do_count(self, line):
        """Count the total number of an object in memory"""
        line_split = line.split()
        all_objects = storage.all()

        count = 0
        if line == "":
            print("** class name missing **")
        elif len(line_split) > 0 and line_split[0] not in ["BaseModel",
                                                           "Amenity",
                                                           "City",
                                                           "Place",
                                                           "Review",
                                                           "State",
                                                           "User"]:
            print("** class doesn't exist **")
        else:
            for value in all_objects.values():
                if type(value) is eval(line_split[0]):
                    count = count + 1
            print(count)

    def do_update(self, line):
        """Updates an instance based on class name and id"""

        line_splts = line.split()
        dict_1 = storage.all()
        if line == "":  # update
            print("** class name missing **")
        elif line_splts[0] not in ["BaseModel",
                                   "Amenity",
                                   "City",
                                   "Place",
                                   "Review",
                                   "State",
                                   "User"
                                   ]:  # update MymOdel
            print("** class doesn't exist **")
        elif len(line_splts) == 1:  # update BaseModel <no id>
            print("** instance id missing **")
        elif len(line_splts) == 2:  # update BaseModel 241545
            key = "{}.{}".format(line_splts[0], line_splts[1])
            if key not in dict_1.keys():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(line_splts) == 3:
            print("** value missing **")
        else:
            key_1 = "{}.{}".format(line_splts[0], line_splts[1])
            if key_1 in dict_1.keys():
                obj_1 = dict_1[key_1]
                obj_replace = line_splts[3].replace('"', '')
                if obj_replace.find(".") > 0:
                    cast = float
                else:
                    cast = int
                if line_splts[2] not in ["updated_at", "id", "created_at"]:
                    try:
                        new_obj_replace = cast(obj_replace)
                    except Exception:
                        new_obj_replace = obj_replace
                    obj_1.__dict__[line_splts[2]] = new_obj_replace
                    dict_1[key_1] = obj_1
                    storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
