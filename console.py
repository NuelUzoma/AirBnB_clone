#!/usr/bin/python3
"""
The console command line intepreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Simple command processor example.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """
        The End of File for the console
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
