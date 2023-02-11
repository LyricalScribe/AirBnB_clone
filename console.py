#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
import json
import os


class HBNBCommand(cmd.Cmd):
    intro = "\n".join(
        [
            "Type 'EOF' or 'quit' to exit the program",
            "Type 'Help' or '?' to see all available commands",
            "------------------------------------------------\n"
        ])
    prompt = '(hbnb) '
    lst_class = ["BaseModel"]
    file = "models.json"

    def emptyline(self):
        return None

    def do_EOF(self, line):
        """End Of File command exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, args):
        """'create' command that Creates a new instance of 'BaseModel'"""
        if not args:
            print("** class name missing **")
        elif args not in self.lst_class:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            model_dict = new_model.to_dict()
            json_list = []

            if os.path.exists(self.file):
                with open(self.file, 'r') as f:
                    json_list = json.load(f)

            json_list.append(model_dict)
            with open(self.file, 'w') as f:
                json.dump(json_list, f, indent=4)
            print(new_model.id)

    def do_show(self, arg):
        """'show' command that  Prints the string representation of an
        instance based on the class name and 'id'"""

        args = arg.split(' ')
        with open(self.file, 'r') as f:
            data = json.load(f)
        all_id = []
        for i in data:
            for k,v in i.items():
                if k == 'id':
                    all_id.append(v)
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.lst_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[1] not in all_id:
            print("** no instance found **")
        elif args[0] in self.lst_class and args[1] in all_id:
            show_id = None
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
