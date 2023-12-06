#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

    def do_emptyline(self, args):
        pass

    if __name__ == '__main__':
         HBNBCommand().cmdloop()
