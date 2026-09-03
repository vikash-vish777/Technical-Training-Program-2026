#WAP to accept week day name and check the entered day is workind day or weekend day

day=input("Enter the day name: ")
if day=="Saturday" or day=="Sunday":
    print(day,"is a weekend day")
elif day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday":
    print(day,"is a working day")
else:
    print("Invalid day name")
