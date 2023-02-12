#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
import json
import os


class HBNBCommand(cmd.Cmd):
    # intro = "\n".join(
    #     [
    #         "Type 'EOF' or 'quit' to exit the program",
    #         "Type 'Help' or '?' to see all available commands",
    #         "------------------------------------------------\n"
    #     ])
    prompt = '(hbnb) '
    lst_class = ["BaseModel"]
    dict_class = {"BaseModel": BaseModel}
    file = "models_dict.json"

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
        all_id = [v for i in data for k, v in i.items() if k == 'id']

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.lst_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[1] not in all_id:
            print("** no instance found **")
        elif args[0] in self.lst_class and args[1] in all_id:
            my_object = [
                BaseModel(**i) for i in data for
                k in i.keys() if i[k] == args[1]
            ][0]
            print(my_object)

    def do_destroy(self, arg):
        """'destroy' command Deletes an instance
        based on the class name and id"""
        args = arg.split(' ')
        with open(self.file, 'r') as f:
            data = json.load(f)
        all_id = [v for i in data for k, v in i.items() if k == 'id']

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.lst_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[1] not in all_id:
            print("** no instance found **")
        elif args[0] in self.lst_class and args[1] in all_id:

            count = 0
            with open(self.file, 'r') as f:
                data = json.load(f)
            for obj in data:
                for key in obj.keys():
                    if obj[key] == args[1]:
                        del(data[count])
                count += 1
            with open(self.file, 'w') as f:
                json.dump(data, f, indent=4)

    def do_all(self, args):
        """'all' command Prints all string representation
        of all instances based or not on the class name."""
        if not args or args in self.lst_class:
            all_lst = []
            with open(self.file, 'r') as f:
                data = json.load(f)
            all_objects = [
                v(**obj) for v in
                self.dict_class.values() for obj in data
                ]

            for obj in all_objects:
                all_lst += [str(obj)]
            print(all_lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """'update' command Updates an instance based on the
        class name and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
            all_id = [v for i in data for k, v in i.items() if k == 'id']

            args = arg.split(" ")
            if not arg:
                print("** class name missing **")
            elif args[0] not in self.lst_class:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif args[1] not in all_id:
                print("** no instance found **")

            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            elif len(args) > 4:
                print(
                    "Usage: update <class name>" +
                    " <id> <attribute name> '<attribute value>'"
                    )

            elif args[0] in self.lst_class and args[1] in all_id:
                my_object = [
                    BaseModel(**i) for i in data for k
                    in i.keys() if i[k] == args[1]
                    ][0]
                my_value = args[3].strip('""')
                setattr(my_object, args[2], my_value)
                class_id = args[0] + " " + args[1]
                updated_dict = my_object.to_dict()
                self.do_destroy(class_id)

                with open(self.file, 'r') as f:
                    new_data = json.load(f)
                new_data.append(updated_dict)

                with open(self.file, 'w') as f:
                    json.dump(new_data, f, indent=4)
        except FileNotFoundError:
            print("You need to Create a file before updating one")
        except UnboundLocalError:
            print("You need to Create a file before updating one")

    def emptyline(self):
        return None

    def do_EOF(self, line):
        """End Of File command exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
