class Employee:
    def __init__(self):
        self.name="prashant jha " # instance variable :-  create a saperate memory

obj1=Employee()#["prashant jha"]
obj2=Employee()#["prashant jha"]
obj3=Employee()#["prashant jha"]

print(obj1.name)
print(obj2.name)
print(obj3.name)

obj1.name="peter"
obj2.name="aditya"
print(obj1.name)
print(obj2.name)
print(obj3.name)




