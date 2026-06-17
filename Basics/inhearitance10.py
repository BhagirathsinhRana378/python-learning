class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):# just write the parent class name to inherit the properties
    pass # pass this line no empty class allowed

class Cat(Mammal):
    def meow(self):
        print("meow")

dog1 =Dog()
dog1.walk()

cat1= Cat()
cat1.meow()
cat1.walk()
