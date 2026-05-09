class Animal:
    def eat(self):
        print("Eating")
    def sleep(self):
        print("sleeping")
class Dog(Animal):
    def bark(self):
        print("barking")
obj=Dog()
obj.eat()
obj.sleep()
obj.bark()

