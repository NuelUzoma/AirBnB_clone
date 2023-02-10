#!/usr/bin/python3
"""
The console command line intepreter
"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Simple command processor example"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """The End of File for the console"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to JSON File"""
        print(BaseModel.id)
        if __class__.__name__ is None:
           print("** class name missing **")
        elif __class__.__name__ is None:
           print("** class doesn't exists **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if __class__.__name__ is None:
            print("** class name missing **")
        if __class__.__name__ is None:
            print("** class doesn't exist **")
        if BaseModel.id is None:
            print("** instance id missing **")
        if not BaseModel.id:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on class name and id"""
        if __class__.__name__ is None:
            print("** class name missing **")
        if __class__.__name__ is None:
            print("** class doesn't exist **")
        if self.id is None:
            print("** instance id missing **")
        if not self.id:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if __class__.__name__ is None:
            print("** class doesn't exist **")
    
    def do_update(self, line):
        """Updates an instance based on class name and id"""
        return "update {} {} {} {} {}.".format(
            self.__class__.__name__, self.id, self.key, self.value)
        if __class__.__name__ is None:
            print("** class name missing **")
        if __class__.__name__ is None:
            print("** class doesn't exist **")
        if BaseModel.id is None:
            print("** instance id missing **")
        if not BaseModel.id:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
