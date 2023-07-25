"""Natalie Ferraro dog.py

dog.py is an example dog dataclass.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Dog:
    """Dog dataclass defines a dog object using datafields name, age, weight, and good."""
    name:str
    age:int
    weight:float
    good:bool

@dataclass
class Pack:
    """Pack dataclass defines a pack object representing a pack of dogs."""
    members: List[Dog]

if __name__ =="__main__":
    dog1 = Dog('Coco', 18, 26.9, True)
    print(dog1.name)
    print(dog1.age)
    print(dog1.weight)
    print(dog1.good)

    dog2 = Dog('Marvin', 7, 13.1, False)
    dog3 = Dog('Lily', 6, 11.3, False)
    dog4 = Dog('Junior', 5, 11.9, True)
    dog5 = Dog('Knuckles', 5, 11.1, True)

    print(dog1)
    print(dog2)
    print(dog3)
    print(dog4)
    print(dog5)

    print(dog1.__match_args__)
    print(dog1.__dataclass_fields__['good'].type)
    pack1 = Pack([dog1, dog2, dog3, dog4, dog5])

    for dog in pack1.__dict__.values():
        print(dog)