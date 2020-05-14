# Creating a Dog Class
#By convention, capitalized names refer to classes in Python
class Dog():
    """A simple attempt to model a dog"""
#A function that is part of a class is a "method"
    def __init__(self, name, age):
        #Initialize name and age attribute.
        #variables with prefix(self.) can be assessed in any method under a class, they're called "attributes"
        self.name = name 
        self.age = age

    def sit(self):
        #Simulate a dog sitting in response to a command.
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        #Simulate rolling over in response to a command.
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 4)
my_dog.sit()
my_dog.roll_over()