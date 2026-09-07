# import time
# n=int(input("enter a number of row:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(0)
#         print(n+1-1,end=" ")
#     print()


# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print(" " * (n-1),end=" ")
#     for j in range(1,i+1):
#         print(" *",end=" ")
#     print()



# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     print("  " * (n - i), end="")

#     for j in range(1, i + 1):
#         print("*", end=" ")

#     print()


# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print("  "*(n-i),end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()  



# for i in "prashant":
#     print(i)



name="prashant"

# for i in range(len(name)-1):
#     print(name[i],end=" ")

for i in range(len(name)):
    print(name[-i-1],end=" ")


name = "prashant"
result = ""

for i in name:
    if i not in result:
        result += i

print(result)