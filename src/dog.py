from dataclasses import dataclass
from typing import List

@dataclass
class Dog:
    """Dog dataclass defines a dog object using datafields name, age, weight, and good."""
    name:str
    age:int
    weight:float
    good:bool

    def __str__(self):
        """__str__ function returns the data of a dog object in a readable formatt."""
        return f"{self.name}, {self.age}, {self.weight}, {self.good}"
    
@dataclass
class Pack:
    """Pack dataclass defines a pack object representing a pack of dogs."""
    members: List[Dog]

    def __str__(self):
        """__str__ function returns the data of a pack object in a readable formatt."""
        return f"{self.members}"

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

    print(dog1.__str__())
    print(dog2.__str__())
    print(dog3.__str__())
    print(dog4.__str__())
    print(dog5.__str__())

    pack1 = Pack([dog1, dog2, dog3, dog4, dog5])
    print(pack1.__str__())