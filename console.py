#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

    if __name__ == '__main__':
         HBNBCommand().cmdloop()
