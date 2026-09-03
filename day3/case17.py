for i in range(1,6):
    if i==3:
        continue
    print(i,6-i)

print("Using zip() function")
for x,j in zip(range(1,6),range(5,0,-1)):
    if x==3 and j==3:
        continue
    print(x,j)