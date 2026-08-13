#instance variable in class
#instance variable depends on state of the object, for every object instance variable.
#creates a separate memory.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayName(self):
        print("Name:", self.name)
        print("Age:", self.age)

obj1 = Student("Niharika", 19)
obj2 = Student("Rana", 23)

obj1.displayName()
obj2.displayName()

#lets change the value of obj1 instance variable
obj1.name = "Niharika Rana"
obj1.displayName()
obj2.displayName()