#!/usr/bin/python3
"""Our Console Module handles all CLI function"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """CLI Processor"""

    prompt = '(hbnb) '
    lst_class = [
        "BaseModel", "User", "State", "City",
        "Place", "Amenity", "Review"
        ]
    lst_cmd = ["show", "count", "all", "destroy", "update"]

    dict_class = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
    file = "models_dict.json"

    def do_create(self, args):
        """'create' command that Creates a new instance of 'BaseModel'"""
        if not args:
            print("** class name missing **")
        elif args not in self.lst_class:
            print("** class doesn't exist **")
        else:
            new_model = self.dict_class[args]()
            storage.save()
            print(new_model.id)

    def do_show(self, arg):
        """'show' command that  Prints the string representation of an
        instance based on the class name and 'id'"""

        args = arg.split(' ')

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.lst_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")

        else:
            all_object = storage.all()

            for v in all_object.values():
                ob_name = v.__class__.__name__
                ob_id = v.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """'destroy' command Deletes an instance
        based on the class name and id"""
        args = arg.split(' ')

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.lst_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """'all' command Prints all string representation
        of all instances based or not on the class name."""
        if not args or args in self.lst_class:
            all_objs = storage.all()
            list_instances = []
            for value in all_objs.values():
                ob_name = value.__class__.__name__
                if not args:
                    list_instances += [value.__str__()]
                if ob_name == args:
                    list_instances += [value.__str__()]
            print(list_instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """'update' command Updates an instance based on the
        class name and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.lst_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for objc in all_objs.values():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_count(self, arg):
        data = storage.all()
        num = 0
        if not arg:
            print(len(data))
            return
        for v in data.values():
            if v.__class__.__name__ == arg:
                num += 1
        print(num)

    def emptyline(self):
        return None

    def do_EOF(self, line):
        """End Of File command exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def precmd(self, line):
        """Handling extra commands for CLI"""

        if '.' in line and '(' in line and ')' in line:
            d_cls = line.split('.')
            d_cmd = d_cls[1].split('(')
            d_arg = d_cmd[1].split(')')
            if '{' and '}' in line:
                u_arg = eval(d_arg[0])

                # u_join = u_arg[1] + "," + u_arg[2]
                u_dct = u_arg[1]
                num = len(u_dct)
                for k, v in u_dct.items():
                    line = (
                        d_cmd[0] + ' ' + d_cls[0] + " " + u_arg[0]
                        + ' ' + str(k) + ' ' + str(v)
                        )
                    if num == 1:
                        return line
                    line2 = (
                        d_cls[0] + " " + u_arg[0] +
                        ' ' + str(k) + ' ' + str(v)
                        )
                    self.do_update(line2)
                    num -= 1
                return line

            if d_cls[0] in self.lst_class and d_cmd[0] in self.lst_cmd:
                line = d_cmd[0] + ' ' + d_cls[0] + " " + d_arg[0]

        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
