class College:
    collegename= "modern colleg" #static variable(1memory)
    def __init__(self):
        self.studentname="prashant"#instance variable (3 seprate memory)


principle= College() #object creation
teacher = College()
accountant= College()

print(principle.collegename,principle.studentname)
print(teacher.collegename,teacher.studentname)
print(accountant.collegename,accountant.studentname)

College.collegename="HBD" # second way to add static variable
principle.studentname="prashant jha"

print(principle.collegename,principle.studentname)
print(teacher.collegename,teacher.studentname)
print(accountant.collegename,accountant.studentname)