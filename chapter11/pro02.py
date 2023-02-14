class Animal:
    animalType = "monkey"

class Pet(Animal):
    color = "white"

class Dog(Pet):
    @staticmethod
    def bark():
        print("bow bow")

d = Dog()
d.bark()
