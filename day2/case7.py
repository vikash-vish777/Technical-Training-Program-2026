#i/p=[1,2,3,4]
#o/p=[24,12,8,6]

mylist=[1,2,3,4]#--------O(1)
result=[]#--------O(1)
for i in range(len(mylist)):#--------O(n) 1
    product=1#--------O(1) 
    for j in range(len(mylist)):#--------O(n) 1
        if i!=j:#--------O(1)  1!=1 false  1!=2 true
            product*=mylist[j]#--------O(1) 
    result.append(product)#--------O(1)

print(result)#--------O(1)