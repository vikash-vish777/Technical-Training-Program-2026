#WAP to accept rating in float and increament the salary base on rating like the test case give below.
# Accept the salary from user

# rating >=1 and <=3 then increament salary by 10%
# rating >=3.1 and<=4 then increament salary by 20%
# rating>=4.1 and then <=5 then increment salary by 30%




salary = float(input("Enter salary: "))
rating = float(input("Enter rating: "))

if rating >= 1 and rating <= 3:
    salary = salary + (salary * 10 / 100)

elif rating >= 3.1 and rating <= 4:
    salary = salary + (salary * 20 / 100)

elif rating >= 4.1 and rating <= 5:
    salary = salary + (salary * 30 / 100)

else:
    print("Invalid rating")
    exit()

print("Incremented salary:", salary)