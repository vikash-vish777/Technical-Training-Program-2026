class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNodeBeginning(self, value):
        nodeValue = Node(value)

        if self.head is None:
            self.head = nodeValue
            self.tail = nodeValue
        else:
            nodeValue.next = self.head
            self.head = nodeValue

    def addNodeEnd(self,value):
        nodeValue=Node(value)
        if self.head is None:
            self.head=nodeValue
            self.tail=nodeValue
        else:
            self.tail.next=nodeValue
            self.tail=nodeValue

    def display(self):
        temp = self.head

        while temp != None:
            print("[", temp.value, "]", "->", end=" ")
            temp = temp.next


linked_obj = linkedList()

linked_obj.addNodeBeginning(10)
linked_obj.addNodeBeginning(5)
linked_obj.addNodeEnd(39)
linked_obj.addNodeBeginning(19)
linked_obj.addNodeBeginning(15)
linked_obj.addNodeEnd(29)

linked_obj.display()