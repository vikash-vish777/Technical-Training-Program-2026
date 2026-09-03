#type of argument
def add(val1,val2):
    print(val1+val2)

add(10,20) #positional argument(calling function with positional argument)


def add(val1,val2):
    return val1+val2

print(add(10,20)) # calling function with positional argument and printing the return value

def add(val1,val2):
    return val1+val2

result=add(10,20) # calling function with positional argument and storing the return value in a variable
print(result) # printing the return value stored in a variable


def arithmetic(val1,val2):
    a=val1+val2
    s=val1-val2 
    m=val1*val2
    d=val1/val2
    return a,s,m,d

result=arithmetic(10,20) # calling function with positional argument and storing the return value in a variable
print(result) # printing the return value stored in a variable



#keyword argument
def personelInfo(firstName,lastName):
    print("First Name:",firstName)
    print("Last Name:",lastName)

personelInfo(firstName="John",lastName="Doe") # calling function with keyword argument


#default argument
def cityName(city='nashik'):
    print("City Name:",city)

cityName("New York") # calling function with positional argument
cityName("Los Angeles") # calling function with keyword argument
cityName() # calling function without argument will use the default value 'nashik'

#variable length argument / variable number of arguments
def stateName(*cityNames):
    print("City Names:",cityNames)

stateName("mumbai", "Nashik", "Pune") # calling function with variable length argument



#  Linear Search

def linearSearch(arr,target):
    for i in range(len(arr)): 
        if arr[i]==target:
            print("Element found at index:",i)
            return
    print("Element not found")


arr=[10,20,30,40,50]
target=40
linearSearch(arr, target) 
