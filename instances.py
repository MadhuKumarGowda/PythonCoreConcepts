import random

class Animal:
    info = "A living organism"

    def __init__(self, name):
        print(f"An Animal has created for {name}")
        self.name = name

class Dog(Animal):  # inheritance
    info = "A dog is little animal"

    def __init__(self, name):
        super().__init__(name)
        print("A dog has cretaed")
        self.magicnumber =  random.randint(1,10)
       

    def bark(self):
        print(f"Barking woof and my name is {self.name} and number is {self.magicnumber} ")

#print(Dog.info)
dog1 = Dog("Pinky")
# dog2 = Dog("Fido")
# dog3 = Dog("Lucky")

#print(dog1.info, dog1.name , dog1.magicnumber)
# print(dog2.name , dog2.magicnumber)
# print(dog3.name , dog3.magicnumber)
# print(dog3.bark())