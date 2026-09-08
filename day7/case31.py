class Node:
    def __init__(self,value):
        self.data=value #[10 | none] [20 | none] [30 | none] 
        self.next=None  #101              102        103

class LinkedList:
    def __init__(self):
        self.head=None

linkedobj= LinkedList()
#creating independent nodes
linkedobj.head=Node(10) #101

second = Node(20) #102
third = Node(30) #103
fourth=Node(40)

#creating  independent node
linkedobj.head.next=second
second.next = third
third.next=fourth

#display Linkedlist

while linkedobj.head != None:
    print("[",linkedobj.head.data,"|",linkedobj.head.next,"]","->",end="")
    linkedobj.head=linkedobj.head.next

