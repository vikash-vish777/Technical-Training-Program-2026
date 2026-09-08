# static variable\

class College:
    college_Name="Delhi University"# statuc variable


obj1=College()#[Delhi univrsity]
obj2=College()
obj3=College()

print(obj1.college_Name)
print(obj2.college_Name)
print(obj3.college_Name)

College.college_Name="mordern univercity" # change the static value

print(obj1.college_Name)
print(obj2.college_Name)
print(obj3.college_Name)