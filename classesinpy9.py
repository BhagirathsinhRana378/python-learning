class Point:
    def move(self):
        print("move")
    def swim(self):
        print("swim")

# we use classes to define new types of method

point1 = Point()
point1.swim()
#Classes

#constructors
# a constructor is a function that gets called at the time of creating an object

class Point:
    def __init__(self,x ,y):
        self.x = x # we use self tp refrence the current object
        self.y = y

    def move(self):
        print("move")
    def swim(self):
        print("swim")

# we use classes to define new types of method

point1 = Point()
point1.swim()