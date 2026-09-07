class student:
    def __init__(self):
        print("i will call automatically when object is created")
    def massege(self):
        print("this is a message from student class")
obj=student()
print(obj) # this will print the memory location of the object
obj.massege() # this will call the massege method