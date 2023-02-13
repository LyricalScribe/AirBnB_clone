#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
# print(all_objs)
print("-- Reloaded objects --")
for obj_id in all_objs.values():
    # obj = all_objs[obj_id]
    # print(obj)
    print(obj_id.__dict__)

# print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
# print(my_model)
