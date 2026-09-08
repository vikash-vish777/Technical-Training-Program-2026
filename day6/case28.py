class Student:
    def __init__(self):
        self.name=input("enter your name:")
        self.rollno=101

    def getdata(self):
        self.mb=963852741789

obj1=Student()
obj1.getdata()
obj1.branch="cs" #addding instance variable by using object
del obj1.rollno #deleteing a instance variable
print(obj1. __dict__)


