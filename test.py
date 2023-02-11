#!/usr/bin/env python3
import json

class MyClass:
    the = 2
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f"[name]: {self.name} \n[age]: {self.age}"

# Create instances of the class
obj1 = MyClass("John", 30)
obj2 = MyClass("Jane", 25)
print(obj1)

