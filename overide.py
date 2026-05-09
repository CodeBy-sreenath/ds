# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child class
class Dog(Animal):
    # Overriding the parent class method
    def sound(self):
        print("Dog barks")

# Creating object of child class
d = Dog()
d.sound()      # Output: Dog barks

# Creating object of parent reference to child object
a = Dog()
a.sound()      # Output: Dog barks