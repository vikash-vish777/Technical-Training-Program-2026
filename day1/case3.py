mylist=[2, 3, 4, 5, 6, 7, 8, 9, 10] #--------O(1)
even=0#--------O(1)
odd=0#--------O(1)
for i in range(len(mylist)):#--------O(n)
    if mylist[i]%2==0:#--------O(1)
        even+=1#--------O(1)
    else:
        odd+=1#--------O(1)
print("Even numbers:", even)#--------O(1)
print("Odd numbers:", odd)#--------O(1)

#total time complexity=O(1)+O(n) =O(n)