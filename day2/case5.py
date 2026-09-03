#i/p=[5,3,9,2,8]
#o/p=maximum is 9 and minimum is 2

mylist=[5,3,9,2,8]#--------O(1)
      # 0 1 2 3 4 
max=mylist[0]#--------O(1)  5
min=mylist[0]#--------O(1)  5  
for i in mylist:#--------O(n)  i=5  i=3
    if i>max:#--------O(1)  5>5 false  3>5 false
        max=i#--------O(1) 
    if i<min:#--------O(1)  5<5 false  3<5 true
        min=i#--------O(1) 3 

print("Maximum is:", max)#--------O(1)
print("Minimum is:", min)#--------O(1)

#total time complexity=O(1)+O(n)=O(n)