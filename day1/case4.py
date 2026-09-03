#i/p=[5,6,0,2,0,1,7]
#o/p=[5,6,2,1,7,0,0] move zero`s in the end of list/array

mylist=[5,6,0,2,0,1,7]#-----------O(1)
temp=0 #-----------O(1)
for i in range(len(mylist)):#-----------O(n)
    if mylist[i]!=0: #----------O(1)
        mylist[temp]=mylist[i] #---------------O(1)
        temp+=1 #-----------O(1)
for i in range(temp, len(mylist)): #-----------O(n)
    mylist[i]=0 #-------O(1)

print(mylist) #-----------O(1)

#total time complexity=O(1)+O(n)=O(n)


for i in mylist:
    if i==0:
        mylist.remove(i)
        mylist.append(0)
print(mylist)